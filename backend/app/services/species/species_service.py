from uuid import UUID

from fastapi import HTTPException, status

from app.repositories.species.species_repository import SpeciesRepository
from app.schemas.species import (
    SpeciesExplorerFilters,
    SpeciesExplorerResponse,
)
from app.schemas.species.species import SpeciesResponse


class SpeciesService:
    def __init__(self, repository: SpeciesRepository):
        self.repository = repository

    def get_species_explorer(
        self,
        filters: SpeciesExplorerFilters,
    ) -> SpeciesExplorerResponse:
        return self.repository.get_species_explorer(filters)

    def get_species_by_id(
        self,
        species_id: UUID,
    ) -> SpeciesResponse:
        species = self.repository.get_by_id(species_id)

        if species is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Species not found",
            )

        return species