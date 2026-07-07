from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


#
# Request Schemas
#
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


#
# Nested Response Schemas
#
class ObservationSpeciesResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    common_name: str
    scientific_name: str
    ebird_code: str


class ObservationLocationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str | None = None


class ObservationUserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str


#
# Main Response Schema
#
class ObservationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID

    observation_datetime: datetime

    count: int

    notes: str | None = None

    species: ObservationSpeciesResponse

    location: ObservationLocationResponse | None = None

    user: ObservationUserResponse

    created_at: datetime

    updated_at: datetime


#
# Paginated Response
#
class ObservationListResponse(BaseModel):
    items: list[ObservationResponse]

    total: int

    page: int

    page_size: int

    total_pages: int