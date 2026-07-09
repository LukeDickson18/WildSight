from uuid import UUID

from pydantic import BaseModel


class SpeciesExplorerSpecies(BaseModel):
    id: UUID

    common_name: str
    scientific_name: str

    image_url: str | None = None
    thumbnail_url: str | None = None

    family_common_name: str | None = None
    order_common_name: str | None = None


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


class SpeciesExplorerResponse(BaseModel):
    items: list[SpeciesExplorerSpecies]

    total: int
    page: int
    page_size: int