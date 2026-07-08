from datetime import datetime

import httpx

from app.core.settings import settings


class WeatherClient:
    """
    Client responsible for communicating with the Open-Meteo APIs.

    This class performs HTTP requests only and returns the raw JSON
    responses. Parsing and business logic are handled by the services.
    """

    def __init__(self) -> None:
        self.timeout = settings.open_meteo_timeout

    def get_archive_weather(
        self,
        latitude: float,
        longitude: float,
        observation_datetime: datetime,
    ) -> dict:
        """
        Retrieve historical hourly weather from the Open-Meteo Archive API.
        """

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "start_date": observation_datetime.strftime("%Y-%m-%d"),
            "end_date": observation_datetime.strftime("%Y-%m-%d"),
            "hourly": ",".join(
                [
                    "temperature_2m",
                    "apparent_temperature",
                    "relative_humidity_2m",
                    "dew_point_2m",
                    "surface_pressure",
                    "cloud_cover",
                    "visibility",
                    "uv_index",
                    "wind_speed_10m",
                    "wind_direction_10m",
                    "wind_gusts_10m",
                    "precipitation",
                    "weather_code",
                ]
            ),
        }

        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.get(
                    settings.open_meteo_base_url,
                    params=params,
                )
                response.raise_for_status()

        except httpx.HTTPError as exc:
            raise ValueError(
                f"Failed to retrieve archive weather: {exc}"
            ) from exc

        return response.json()

    def get_current_weather(
        self,
        latitude: float,
        longitude: float,
    ) -> dict:
        """
        Retrieve the current weather and today's forecast from the
        Open-Meteo Forecast API.
        """

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": ",".join(
                [
                    "temperature_2m",
                    "apparent_temperature",
                    "relative_humidity_2m",
                    "precipitation",
                    "cloud_cover",
                    "wind_speed_10m",
                    "wind_direction_10m",
                    "weather_code",
                ]
            ),
        }

        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.get(
                    settings.open_meteo_forecast_url,
                    params=params,
                )
                response.raise_for_status()

        except httpx.HTTPError as exc:
            raise ValueError(
                f"Failed to retrieve current weather: {exc}"
            ) from exc

        return response.json()