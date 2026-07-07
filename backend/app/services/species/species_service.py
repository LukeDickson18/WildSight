from uuid import UUID

from fastapi import HTTPException, status

from app.repositories.species.species_repository import SpeciesRepository
from app.schemas.species.species import SpeciesListResponse, SpeciesResponse


class SpeciesService:
    def __init__(self, repository: SpeciesRepository):
        self.repository = repository

    def get_species(
        self,
        page: int,
        page_size: int,
    ) -> SpeciesListResponse:
        species, total = self.repository.get_species(
            page=page,
            page_size=page_size,
        )

        return SpeciesListResponse(
            items=species,
            total=total,
            page=page,
            page_size=page_size,
        )

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

    def search_species(
        self,
        query: str,
        page: int,
        page_size: int,
    ) -> SpeciesListResponse:
        species, total = self.repository.search(
            query_text=query,
            page=page,
            page_size=page_size,
        )

        return SpeciesListResponse(
            items=species,
            total=total,
            page=page,
            page_size=page_size,
        )