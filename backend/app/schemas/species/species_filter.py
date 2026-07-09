from uuid import UUID

from pydantic import BaseModel


class SpeciesExplorerFilters(BaseModel):
    search: str | None = None

    order_id: UUID | None = None
    family_id: UUID | None = None
    country_id: UUID | None = None

    latitude: float | None = None
    longitude: float | None = None
    radius_km: float | None = None

    hotspot_id: UUID | None = None

    page: int = 1
    page_size: int = 25