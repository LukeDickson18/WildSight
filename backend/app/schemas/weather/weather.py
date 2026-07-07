from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WeatherData(BaseModel):
    """
    Weather conditions for a single observation.

    This schema is used by the WeatherService after retrieving
    historical weather from Open-Meteo and before persisting
    the data to the database.
    """

    observation_datetime: datetime

    temperature: float | None = None
    apparent_temperature: float | None = None

    relative_humidity: float | None = None
    dew_point: float | None = None

    pressure: float | None = None
    cloud_cover: float | None = None
    visibility: float | None = None
    uv_index: float | None = None

    wind_speed: float | None = None
    wind_direction: float | None = None
    wind_gust: float | None = None

    precipitation: float | None = None

    weather_code: int | None = None
    weather_description: str | None = None

    model_config = ConfigDict(from_attributes=True)