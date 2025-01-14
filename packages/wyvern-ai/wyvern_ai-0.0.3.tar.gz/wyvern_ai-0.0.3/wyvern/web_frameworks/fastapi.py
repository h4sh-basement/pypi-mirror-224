# -*- coding: utf-8 -*-
import logging
import time
from contextlib import asynccontextmanager
from typing import Dict, Type

import uvicorn
from ddtrace import tracer
from fastapi import BackgroundTasks, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from wyvern import request_context
from wyvern.aws.kinesis import KinesisFirehoseStream, wyvern_kinesis_firehose
from wyvern.components.api_route_component import APIRouteComponent
from wyvern.config import settings
from wyvern.core.httpx import httpx_client
from wyvern.entities.request import BaseWyvernRequest
from wyvern.event_logging import event_logger
from wyvern.exceptions import WyvernError, WyvernRouteRegistrationError
from wyvern.wyvern_request import WyvernRequest

logger = logging.getLogger(__name__)


def _dedupe_slash(path: str) -> str:
    return path.replace("//", "/")


def _massage_path(path: str) -> str:
    massaged_path = _dedupe_slash(path)
    if massaged_path and massaged_path[0] != "/":
        massaged_path = "/" + massaged_path
    if massaged_path and massaged_path[-1] == "/":
        massaged_path = massaged_path[:-1]
    return massaged_path


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        httpx_client.start()
        yield
    finally:
        await httpx_client.stop()


class WyvernFastapi:
    """
    endpoint input:
        the built WyvernPipeline
        the request input schema
        the request output schema
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 8000) -> None:
        self.app = FastAPI(lifespan=lifespan)
        self.host = host
        self.port = port

        @self.app.exception_handler(WyvernError)
        async def wyvern_exception_handler(request: Request, exc: WyvernError):
            return JSONResponse(
                status_code=400,
                content={
                    "detail": str(exc),
                    "error_code": exc.error_code,
                },
            )

        @self.app.get("/healthcheck")
        async def healthcheck() -> Dict[str, str]:
            return {"status": "OK"}

        @self.app.middleware("http")
        async def request_middleware(request: Request, call_next):
            start_time = time.time()
            response = await call_next(request)
            if request.url.path == "/healthcheck":
                return response
            process_time_ms = (time.time() - start_time) * 1000
            logger.info(
                f"process_time={process_time_ms} ms, "
                f"method={request.method}, url={request.url.path}, status_code={response.status_code}",
            )
            return response

    async def register_route(
        self,
        route_component: Type[APIRouteComponent],
    ) -> None:
        """
        Support post request
        """
        if not issubclass(route_component, APIRouteComponent):
            raise WyvernRouteRegistrationError(component=route_component)

        root_component = route_component()
        await root_component.initialize_wrapper()
        path = _massage_path(f"/api/{root_component.API_VERSION}/{root_component.PATH}")

        @self.app.post(
            path,
            response_model=root_component.RESPONSE_SCHEMA_CLASS,
            response_model_exclude_none=True,
        )
        async def post(
            fastapi_request: Request,
            background_tasks: BackgroundTasks,
        ) -> root_component.RESPONSE_SCHEMA_CLASS:  # type: ignore
            with tracer.trace("wyvern.get_json"):
                json = await fastapi_request.json()

            try:
                with tracer.trace("wyvern.parse_json"):
                    data = root_component.REQUEST_SCHEMA_CLASS(**json)
                # from pyinstrument import Profiler
                # profiler = Profiler(async_mode="enabled")
                # profiler.start()
                request_id = None
                if isinstance(data, BaseWyvernRequest):
                    request_id = data.request_id
                wyvern_req = WyvernRequest.parse_fastapi_request(
                    json=data,
                    req=fastapi_request,
                    request_id=request_id,
                )
                request_context.set(wyvern_req)

                await root_component.warm_up(data)
                output = await root_component.execute(data)

                background_tasks.add_task(
                    wyvern_kinesis_firehose.put_record_batch_callable,
                    KinesisFirehoseStream.EVENT_STREAM,
                    # TODO (suchintan): "invariant" list error
                    event_logger.get_logged_events_generator(),  # type: ignore
                )

                # profiler.stop()
                # profiler.print(show_all=True)
            except ValidationError as e:
                logger.exception(f"Unexpected error error={e} request_payload={json}")
                raise HTTPException(status_code=422, detail=e.errors())
            except Exception as e:
                logger.exception(f"Unexpected error error={e} request_payload={json}")
                raise HTTPException(status_code=500, detail=str(e))
            finally:
                request_context.reset()
            if not output:
                raise HTTPException(status_code=500, detail="something is wrong")
            logger.info(
                f"path={path}, request_payload={json}, response_payload={output}",
            )
            return output

    def run(self) -> None:
        config = uvicorn.Config(
            self.app,
            host=self.host,
            port=self.port,
            timeout_keep_alive=settings.SERVER_TIMEOUT,
        )
        uvicorn_server = uvicorn.Server(config=config)
        uvicorn_server.run()
