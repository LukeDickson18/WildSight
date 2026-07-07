from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.species.species_repository import SpeciesRepository
from app.schemas.species.species import SpeciesListResponse, SpeciesResponse
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
    "",
    response_model=SpeciesListResponse,
    summary="Get all species",
)
def get_species(
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=100),
    service: SpeciesService = Depends(get_species_service),
) -> SpeciesListResponse:
    return service.get_species(
        page=page,
        page_size=page_size,
    )


@router.get(
    "/search",
    response_model=SpeciesListResponse,
    summary="Search species",
)
def search_species(
    q: str = Query(..., min_length=1, description="Search by common name, scientific name or eBird code"),
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=100),
    service: SpeciesService = Depends(get_species_service),
) -> SpeciesListResponse:
    return service.search_species(
        query=q,
        page=page,
        page_size=page_size,
    )


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