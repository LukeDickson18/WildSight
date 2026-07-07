from __future__ import annotations

import math
from datetime import date
from uuid import UUID

from fastapi import HTTPException, status

from app.models.observation import Observation
from app.repositories.locations import LocationRepository
from app.repositories.observations import ObservationRepository
from app.schemas.locations.location import LocationCreate
from app.schemas.observations.observations import (
    ObservationCreate,
    ObservationListResponse,
    ObservationResponse,
    ObservationUpdate,
)
from app.services.locations.location_service import LocationService


class ObservationService:
    def __init__(
        self,
        repository: ObservationRepository,
        location_repository: LocationRepository,
    ):
        self.repository = repository
        self.location_service = LocationService(location_repository)

    def get_observations(
        self,
        *,
        user_id: UUID,
        page: int,
        page_size: int,
        search: str | None = None,
        species_id: UUID | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
        sort: str = "newest",
    ) -> ObservationListResponse:

        observations, total = self.repository.get_observations(
            user_id=user_id,
            page=page,
            page_size=page_size,
            search=search,
            species_id=species_id,
            start_date=start_date,
            end_date=end_date,
            sort=sort,
        )

        return ObservationListResponse(
            items=observations,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=max(1, math.ceil(total / page_size)),
        )

    def get_observation_by_id(
        self,
        observation_id: UUID,
    ) -> ObservationResponse:

        observation = self.repository.get_by_id(observation_id)

        if observation is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Observation not found",
            )

        return observation

    def create_observation(
        self,
        *,
        data: ObservationCreate,
        user_id: UUID,
    ) -> ObservationResponse:

        location = self.location_service.create_location(
            LocationCreate(
                latitude=data.latitude,
                longitude=data.longitude,
            )
        )

        observation = Observation(
            user_id=user_id,
            species_id=data.species_id,
            location_id=location.id,
            observation_datetime=data.observation_datetime,
            count=data.count,
            notes=data.notes,
        )

        return self.repository.create(observation)

    def update_observation(
        self,
        *,
        observation_id: UUID,
        data: ObservationUpdate,
    ) -> ObservationResponse:

        observation = self.repository.get_by_id(observation_id)

        if observation is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Observation not found",
            )

        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(observation, field, value)

        return self.repository.update(observation)

    def delete_observation(
        self,
        observation_id: UUID,
    ) -> None:

        observation = self.repository.get_by_id(observation_id)

        if observation is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Observation not found",
            )

        self.repository.delete(observation)