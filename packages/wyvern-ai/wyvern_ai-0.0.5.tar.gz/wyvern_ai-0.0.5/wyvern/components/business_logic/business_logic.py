# -*- coding: utf-8 -*-
from __future__ import annotations

import logging
from datetime import datetime
from typing import Generic, List

from ddtrace import tracer
from pydantic.generics import GenericModel

from wyvern import request_context
from wyvern.components.component import Component
from wyvern.components.events.events import EntityEventData, EventType, LoggedEvent
from wyvern.components.helpers.sorting import SortingComponent
from wyvern.entities.candidate_entities import (
    GENERALIZED_WYVERN_ENTITY,
    ScoredCandidate,
)
from wyvern.event_logging import event_logger
from wyvern.wyvern_typing import REQUEST_ENTITY

logger = logging.getLogger(__name__)


class BusinessLogicEventData(EntityEventData):
    business_logic_pipeline_order: int
    business_logic_name: str
    old_score: float
    new_score: float


class BusinessLogicEvent(LoggedEvent[BusinessLogicEventData]):
    event_type: EventType = EventType.BUSINESS_LOGIC


class BusinessLogicRequest(
    GenericModel,
    Generic[GENERALIZED_WYVERN_ENTITY, REQUEST_ENTITY],
):
    request: REQUEST_ENTITY
    scored_candidates: List[ScoredCandidate[GENERALIZED_WYVERN_ENTITY]]

    # TODO (suchintan): Give business logic layer access to the feature map in the future
    # feature_map: FeatureMap


# TODO (suchintan): Possibly delete this now that events are gone
class BusinessLogicResponse(
    GenericModel,
    Generic[GENERALIZED_WYVERN_ENTITY, REQUEST_ENTITY],
):
    request: BusinessLogicRequest[GENERALIZED_WYVERN_ENTITY, REQUEST_ENTITY]
    adjusted_candidates: List[ScoredCandidate[GENERALIZED_WYVERN_ENTITY]]


class BusinessLogicComponent(
    Component[
        BusinessLogicRequest[GENERALIZED_WYVERN_ENTITY, REQUEST_ENTITY],
        List[ScoredCandidate[GENERALIZED_WYVERN_ENTITY]],
    ],
    Generic[GENERALIZED_WYVERN_ENTITY, REQUEST_ENTITY],
):
    """
    A component that performs business logic on an entity with a set of candidates

    The request itself could contain more than just entities, for example it may contain a query and so on
    """

    pass


class BusinessLogicPipeline(
    Component[
        BusinessLogicRequest[GENERALIZED_WYVERN_ENTITY, REQUEST_ENTITY],
        BusinessLogicResponse[GENERALIZED_WYVERN_ENTITY, REQUEST_ENTITY],
    ],
    Generic[GENERALIZED_WYVERN_ENTITY, REQUEST_ENTITY],
):
    """
    Steps through a series of business logic components and returns the final output

    This operation is fully chained, meaning that the output of each business logic component is passed
        as an input to the next business logic component
    """

    def __init__(
        self,
        *upstreams: BusinessLogicComponent[GENERALIZED_WYVERN_ENTITY, REQUEST_ENTITY],
        name: str,
    ):
        self.ordered_upstreams = upstreams
        self.sorting_component: SortingComponent = SortingComponent(
            name="business_logic_sorting",
        )
        super().__init__(self.sorting_component, *upstreams, name=name)

    @tracer.wrap(name="BusinessLogicPipeline.execute")
    async def execute(
        self,
        input: BusinessLogicRequest[GENERALIZED_WYVERN_ENTITY, REQUEST_ENTITY],
        **kwargs,
    ) -> BusinessLogicResponse[GENERALIZED_WYVERN_ENTITY, REQUEST_ENTITY]:
        argument = input

        # Make sure that the inputted candidates are actually sorted
        output = await self.sorting_component.execute(input.scored_candidates)

        for (pipeline_index, upstream) in enumerate(self.ordered_upstreams):
            old_scores = [candidate.score for candidate in argument.scored_candidates]

            # this output might have the same reference as the argument.scored_candidates
            output = await upstream.execute(input=argument, **kwargs)

            # TODO (suchintan): This currently assumes that the
            #  output order is unchanged by the business logic component
            #  This is not necessarily true, so we should fix this in the future

            # TODO (suchintan): Make this properly async -- right now it's fast enough
            # where we don't have to care, but in the future we might
            extracted_events: List[
                BusinessLogicEvent
            ] = self.extract_business_logic_events(
                output,
                pipeline_index,
                upstream.name,
                argument.request.request_id,
                old_scores,
            )

            def log_events(
                extracted_events: List[BusinessLogicEvent] = extracted_events,
            ):
                return extracted_events

            # TODO (suchintan): "invariant" list error
            event_logger.log_events(log_events)  # type: ignore
            output = await self.sorting_component.execute(output)

            argument = BusinessLogicRequest(
                request=input.request,
                scored_candidates=output,
            )

        return BusinessLogicResponse(
            request=input,
            adjusted_candidates=output,
        )

    def extract_business_logic_events(
        self,
        output: List[ScoredCandidate[GENERALIZED_WYVERN_ENTITY]],
        pipeline_index: int,
        upstream_name: str,
        request_id: str,
        old_scores: List[float],
    ) -> List[BusinessLogicEvent]:
        timestamp = datetime.utcnow()
        events = [
            BusinessLogicEvent(
                request_id=request_id,
                api_source=request_context.ensure_current_request().url_path,
                event_timestamp=timestamp,
                event_data=BusinessLogicEventData(
                    business_logic_pipeline_order=pipeline_index,
                    business_logic_name=upstream_name,
                    old_score=old_scores[j],
                    new_score=output[j].score,
                    entity_identifier=candidate.entity.identifier.identifier,
                    entity_identifier_type=candidate.entity.identifier.identifier_type,
                ),
            )
            for (j, candidate) in enumerate(output)
            if output[j].score != old_scores[j]
        ]

        return events
