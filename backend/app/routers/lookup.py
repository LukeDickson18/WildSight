from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.species.lookup_repository import LookupRepository
from app.schemas.species.lookup import (
    CountryLookup,
    FamilyLookup,
    HotspotLookup,
    OrderLookup,
)
from app.services.species.lookup_service import LookupService

router = APIRouter(
    prefix="/species/lookup",
    tags=["Species Lookup"],
)


def get_lookup_service(
    db: Session = Depends(get_db),
) -> LookupService:
    """Dependency that provides a LookupService instance."""
    repository = LookupRepository(db)
    return LookupService(repository)


@router.get(
    "/countries",
    response_model=list[CountryLookup],
    summary="Get all countries",
)
def get_countries(
    service: LookupService = Depends(get_lookup_service),
) -> list[CountryLookup]:
    return service.get_countries()


@router.get(
    "/orders",
    response_model=list[OrderLookup],
    summary="Get all taxonomic orders",
)
def get_orders(
    service: LookupService = Depends(get_lookup_service),
) -> list[OrderLookup]:
    return service.get_orders()


@router.get(
    "/families",
    response_model=list[FamilyLookup],
    summary="Get all families",
)
def get_families(
    service: LookupService = Depends(get_lookup_service),
) -> list[FamilyLookup]:
    return service.get_families()


@router.get(
    "/hotspots",
    response_model=list[HotspotLookup],
    summary="Get all hotspots",
)
def get_hotspots(
    service: LookupService = Depends(get_lookup_service),
) -> list[HotspotLookup]:
    return service.get_hotspots()