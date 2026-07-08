from uuid import UUID

from pydantic import BaseModel


class SpeciesExplorerSpecies(BaseModel):
    id: UUID
    common_name: str
    image_url: str | None
    thumbnail_url: str | None


class SpeciesExplorerGroup(BaseModel):
    name: str
    scientific_name: str
    species: list[SpeciesExplorerSpecies]


class SpeciesExplorerResponse(BaseModel):
    groups: list[SpeciesExplorerGroup]