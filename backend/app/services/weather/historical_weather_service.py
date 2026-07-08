from datetime import datetime

from app.schemas.weather.weather import WeatherData
from app.enrichment.weather import WeatherClient
from app.services.weather.weather_codes import WEATHER_CODES


class HistoricalWeatherService:
    """
    Service responsible for retrieving historical weather data from the
    Open-Meteo Archive API.

    This service contains business logic only. HTTP communication is
    delegated to the WeatherClient.
    """

    def __init__(self) -> None:
        self.client = WeatherClient()

    def get_historical_weather(
        self,
        latitude: float,
        longitude: float,
        observation_datetime: datetime,
    ) -> WeatherData:
        """
        Retrieve weather conditions for the supplied coordinates and
        observation datetime.
        """

        data = self.client.get_archive_weather(
            latitude=latitude,
            longitude=longitude,
            observation_datetime=observation_datetime,
        )

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

        weather_code = hourly["weather_code"][index]

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
            weather_code=weather_code,
            weather_description=WEATHER_CODES.get(weather_code),
        )