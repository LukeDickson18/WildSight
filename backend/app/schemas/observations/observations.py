from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ObservationCreate(BaseModel):
    species_id: UUID

    latitude: float
    longitude: float

    observation_datetime: datetime

    count: int = 1
    notes: str | None = None


class ObservationUpdate(BaseModel):
    observation_datetime: datetime | None = None
    count: int | None = None
    notes: str | None = None


class ObservationSpeciesResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    common_name: str
    scientific_name: str
    ebird_code: str


class ObservationLocationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str | None


class ObservationUserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str


class ObservationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID

    observation_datetime: datetime
    count: int
    notes: str | None

    species: ObservationSpeciesResponse
    location: ObservationLocationResponse | None
    user: ObservationUserResponse

    created_at: datetime
    updated_at: datetime


class ObservationListResponse(BaseModel):
    items: list[ObservationResponse]
    total: int
    page: int
    page_size: int