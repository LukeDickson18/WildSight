from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.species.species_repository import SpeciesRepository
from app.schemas.species import (
    SpeciesExplorerFilters,
    SpeciesExplorerResponse,
    SpeciesResponse,
)
from app.services.species import SpeciesService

router = APIRouter(
    prefix="/species",
    tags=["Species"],
)


def get_species_service(
    db: Session = Depends(get_db),
) -> SpeciesService:
    """Dependency that provides a SpeciesService instance."""
    repository = SpeciesRepository(db)
    return SpeciesService(repository)


@router.get(
    "/explorer",
    response_model=SpeciesExplorerResponse,
    summary="Get species explorer",
)
def get_species_explorer(
    filters: SpeciesExplorerFilters = Depends(),
    service: SpeciesService = Depends(get_species_service),
) -> SpeciesExplorerResponse:
    return service.get_species_explorer(filters)


@router.get(
    "/{species_id}",
    response_model=SpeciesResponse,
    summary="Get a species by ID",
)
def get_species_by_id(
    species_id: UUID,
    service: SpeciesService = Depends(get_species_service),
) -> SpeciesResponse:
    return service.get_species_by_id(species_id)