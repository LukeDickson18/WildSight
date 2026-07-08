from fastapi import APIRouter

from app.schemas.weather.current_weather import CurrentWeatherData
from app.services.weather.current_weather_service import (
    CurrentWeatherService,
)

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)

service = CurrentWeatherService()


@router.get(
    "/current",
    response_model=CurrentWeatherData,
)
def get_current_weather(
    latitude: float,
    longitude: float,
) -> CurrentWeatherData:
    return service.get_current_weather(
        latitude=latitude,
        longitude=longitude,
    )