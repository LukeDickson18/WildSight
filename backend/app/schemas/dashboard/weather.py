from pydantic import BaseModel

class DashboardWeatherResponse(BaseModel):
    temperature: float
    apparent_temperature: float
    relative_humidity: float

    wind_speed: float
    wind_direction: float

    cloud_cover: float
    precipitation: float

    weather_description: str