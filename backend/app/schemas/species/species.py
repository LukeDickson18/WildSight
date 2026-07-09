from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str


class FamilyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    family_code: str
    common_name: str
    scientific_name: str
    order: OrderResponse


class SpeciesResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    ebird_code: str
    common_name: str
    scientific_name: str
    category: str
    wildlife_group: str

    # iNaturalist
    inat_taxon_id: int | None
    image_url: str | None
    thumbnail_url: str | None
    image_license: str | None
    image_attribution: str | None
    image_source: str | None

    family: FamilyResponse


class SpeciesListResponse(BaseModel):
    items: list[SpeciesResponse]
    total: int
    page: int
    page_size: int