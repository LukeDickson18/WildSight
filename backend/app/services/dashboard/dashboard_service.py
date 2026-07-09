from app.repositories.dashboard import DashboardRepository
from app.schemas.dashboard import (
    DashboardResponse,
    DashboardWeatherResponse,
)
from app.services.weather import CurrentWeatherService


class DashboardService:
    def __init__(
        self,
        repository: DashboardRepository,
    ):
        self.repository = repository
        self.weather_service = CurrentWeatherService()

    def get_dashboard(self) -> DashboardResponse:
        """
        Returns only the dashboard statistics.

        Weather is loaded separately based on the current
        map location.
        """

        stats = self.repository.get_dashboard_stats()

        return DashboardResponse(
            total_observations=stats["total_observations"],
            species_seen=stats["species_seen"],
            hotspots_visited=stats["hotspots_visited"],
            countries_visited=stats["countries_visited"],
        )

    def get_weather(
        self,
        latitude: float,
        longitude: float,
    ) -> DashboardWeatherResponse:
        """
        Returns the current weather for an arbitrary map location.
        """

        weather = self.weather_service.get_current_weather(
            latitude=latitude,
            longitude=longitude,
        )

        return DashboardWeatherResponse(
            temperature=weather.temperature,
            apparent_temperature=weather.apparent_temperature,
            relative_humidity=weather.relative_humidity,
            wind_speed=weather.wind_speed,
            wind_direction=weather.wind_direction,
            cloud_cover=weather.cloud_cover,
            precipitation=weather.precipitation,
            weather_description=weather.weather_description,
        )