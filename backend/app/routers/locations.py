from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.locations import LocationRepository
from app.schemas.locations import (
    LocationListResponse,
    LocationResponse,
)
from app.services.locations import LocationService

router = APIRouter(
    prefix="/locations",
    tags=["Locations"],
)


def get_location_service(
    db: Session = Depends(get_db),
) -> LocationService:
    repository = LocationRepository(db)
    return LocationService(repository)


@router.get(
    "",
    response_model=LocationListResponse,
    summary="Get locations",
)
def get_locations(
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=100),
    service: LocationService = Depends(get_location_service),
) -> LocationListResponse:
    return service.get_locations(
        page=page,
        page_size=page_size,
    )


@router.get(
    "/{location_id}",
    response_model=LocationResponse,
    summary="Get location by ID",
)
def get_location(
    location_id: UUID,
    service: LocationService = Depends(get_location_service),
) -> LocationResponse:
    return service.get_location_by_id(location_id)


@router.get(
    "/nearby",
    response_model=LocationListResponse,
    summary="Get nearby locations",
)
def get_nearby_locations(
    latitude: float = Query(..., ge=-90, le=90),
    longitude: float = Query(..., ge=-180, le=180),
    radius: int = Query(
        5000,
        gt=0,
        le=50000,
        description="Search radius in metres",
    ),
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=100),
    service: LocationService = Depends(get_location_service),
) -> LocationListResponse:
    return service.get_nearby_locations(
        latitude=latitude,
        longitude=longitude,
        radius=radius,
        page=page,
        page_size=page_size,
    )