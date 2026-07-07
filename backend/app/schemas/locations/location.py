from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class LocationCreate(BaseModel):
    latitude: float
    longitude: float

    name: str | None = None
    country: str | None = None
    state_province: str | None = None
    municipality: str | None = None
    locality: str | None = None


class LocationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID

    name: str | None
    country: str | None
    state_province: str | None
    municipality: str | None
    locality: str | None

    latitude: float
    longitude: float

    created_at: datetime
    updated_at: datetime