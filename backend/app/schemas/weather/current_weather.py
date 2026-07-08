from pydantic import BaseModel


class CurrentWeatherData(BaseModel):
    """
    Current weather conditions returned by the Open-Meteo Forecast API.
    """

    temperature: float | None = None
    apparent_temperature: float | None = None

    relative_humidity: float | None = None

    wind_speed: float | None = None
    wind_direction: float | None = None

    cloud_cover: float | None = None
    precipitation: float | None = None

    weather_code: int | None = None
    weather_description: str | None = None