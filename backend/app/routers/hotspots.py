from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.hotspots import HotspotRepository
from app.schemas.hotspots import (
    HotspotListResponse,
    HotspotResponse,
)
from app.services.hotspots import HotspotService

router = APIRouter(
    prefix="/hotspots",
    tags=["Hotspots"],
)


def get_hotspot_service(
    db: Session = Depends(get_db),
) -> HotspotService:
    repository = HotspotRepository(db)
    return HotspotService(repository)


@router.get(
    "",
    response_model=HotspotListResponse,
    summary="Get hotspots",
)
def get_hotspots(
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=100),
    service: HotspotService = Depends(get_hotspot_service),
) -> HotspotListResponse:
    return service.get_hotspots(
        page=page,
        page_size=page_size,
    )


@router.get(
    "/nearby",
    response_model=HotspotListResponse,
    summary="Get nearby hotspots",
)
def get_nearby_hotspots(
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
    service: HotspotService = Depends(get_hotspot_service),
) -> HotspotListResponse:
    return service.get_nearby_hotspots(
        latitude=latitude,
        longitude=longitude,
        radius=radius,
        page=page,
        page_size=page_size,
    )


@router.get(
    "/{hotspot_id}",
    response_model=HotspotResponse,
    summary="Get hotspot by ID",
)
def get_hotspot(
    hotspot_id: UUID,
    service: HotspotService = Depends(get_hotspot_service),
) -> HotspotResponse:
    return service.get_hotspot_by_id(
        hotspot_id,
    )