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
    family: FamilyResponse


class SpeciesListResponse(BaseModel):
    items: list[SpeciesResponse]
    total: int
    page: int
    page_size: int