from datetime import datetime

import httpx

from app.core.settings import settings
from app.schemas.weather import WeatherData

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with hail",
    99: "Severe thunderstorm with hail",
}


class WeatherService:
    """
    Service responsible for retrieving historical weather data from
    the Open-Meteo Archive API.

    This service does not interact with the database.
    """

    def get_weather(
        self,
        latitude: float,
        longitude: float,
        observation_datetime: datetime,
    ) -> WeatherData:
        """
        Retrieve weather conditions for the supplied coordinates
        and observation datetime.
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
            with httpx.Client(
                timeout=settings.open_meteo_timeout,
            ) as client:
                response = client.get(
                    settings.open_meteo_base_url,
                    params=params,
                )

                response.raise_for_status()

        except httpx.HTTPError as exc:
            raise ValueError(
                f"Failed to retrieve weather data: {exc}"
            ) from exc

        data = response.json()

        hourly = data.get("hourly")

        if hourly is None:
            raise ValueError("No hourly weather data returned.")

        target_hour = (
            observation_datetime.replace(
                minute=0,
                second=0,
                microsecond=0,
            ).strftime("%Y-%m-%dT%H:00")
        )

        try:
            index = hourly["time"].index(target_hour)
        except ValueError as exc:
            raise ValueError(
                "Weather data for the observation time could not be found."
            ) from exc

        return WeatherData(
            observation_datetime=observation_datetime,
            temperature=hourly["temperature_2m"][index],
            apparent_temperature=hourly["apparent_temperature"][index],
            relative_humidity=hourly["relative_humidity_2m"][index],
            dew_point=hourly["dew_point_2m"][index],
            pressure=hourly["surface_pressure"][index],
            cloud_cover=hourly["cloud_cover"][index],
            visibility=hourly["visibility"][index],
            uv_index=hourly["uv_index"][index],
            wind_speed=hourly["wind_speed_10m"][index],
            wind_direction=hourly["wind_direction_10m"][index],
            wind_gust=hourly["wind_gusts_10m"][index],
            precipitation=hourly["precipitation"][index],
            weather_code=hourly["weather_code"][index],
            weather_description=self.get_weather_description(
                hourly["weather_code"][index]
            ),
        )

    @staticmethod
    def get_weather_description(
        weather_code: int | None,
    ) -> str | None:
        """
        Convert Open-Meteo weather codes into a readable description.
        """

        return WEATHER_CODES.get(weather_code)