from uuid import UUID

from pydantic import BaseModel, ConfigDict


class HotspotResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    ebird_id: str
    name: str
    source: str
    latitude: float
    longitude: float


class HotspotListResponse(BaseModel):
    items: list[HotspotResponse]
    total: int
    page: int
    page_size: int