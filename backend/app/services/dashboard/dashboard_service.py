from app.repositories.dashboard import DashboardRepository
from app.schemas.dashboard import (
    DashboardResponse,
    DashboardWeatherResponse,
)
from app.services.weather import CurrentWeatherService


# Temporary default location (Stellenbosch)
DEFAULT_LATITUDE = -33.9321
DEFAULT_LONGITUDE = 18.8602


class DashboardService:
    def __init__(
        self,
        repository: DashboardRepository,
    ):
        self.repository = repository
        self.weather_service = CurrentWeatherService()

    def get_dashboard(self) -> DashboardResponse:
        stats = self.repository.get_dashboard_stats()

        current_weather = self.weather_service.get_current_weather(
            latitude=DEFAULT_LATITUDE,
            longitude=DEFAULT_LONGITUDE,
        )

        return DashboardResponse(
            total_observations=stats["total_observations"],
            species_seen=stats["species_seen"],
            hotspots_visited=stats["hotspots_visited"],
            countries_visited=stats["countries_visited"],
            weather=DashboardWeatherResponse(
                temperature=current_weather.temperature,
                apparent_temperature=current_weather.apparent_temperature,
                relative_humidity=current_weather.relative_humidity,
                wind_speed=current_weather.wind_speed,
                wind_direction=current_weather.wind_direction,
                cloud_cover=current_weather.cloud_cover,
                precipitation=current_weather.precipitation,
                weather_description=current_weather.weather_description,
            ),
        )