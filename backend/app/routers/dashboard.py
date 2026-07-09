from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.dashboard import DashboardRepository
from app.schemas.dashboard import (
    DashboardResponse,
    DashboardWeatherResponse,
)
from app.services.dashboard import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


def get_dashboard_service(
    db: Session = Depends(get_db),
) -> DashboardService:
    repository = DashboardRepository(db)
    return DashboardService(repository)


@router.get(
    "",
    response_model=DashboardResponse,
    summary="Get dashboard statistics",
)
def get_dashboard(
    service: DashboardService = Depends(get_dashboard_service),
) -> DashboardResponse:
    return service.get_dashboard()


@router.get(
    "/weather",
    response_model=DashboardWeatherResponse,
    summary="Get weather for a map location",
)
def get_weather(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    service: DashboardService = Depends(get_dashboard_service),
) -> DashboardWeatherResponse:
    return service.get_weather(
        latitude=lat,
        longitude=lon,
    )