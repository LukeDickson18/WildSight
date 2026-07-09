from app.schemas.weather.current_weather import CurrentWeatherData
from app.enrichment.weather import WeatherClient
from app.services.weather.weather_codes import WEATHER_CODES


class CurrentWeatherService:
    """
    Service responsible for retrieving current weather conditions from
    the Open-Meteo Forecast API.

    This service contains business logic only. HTTP communication is
    delegated to the WeatherClient.
    """

    def __init__(self) -> None:
        self.client = WeatherClient()

    def get_current_weather(
        self,
        latitude: float,
        longitude: float,
    ) -> CurrentWeatherData:
        """
        Retrieve the current weather for the supplied coordinates.
        """

        data = self.client.get_current_weather(
            latitude=latitude,
            longitude=longitude,
        )

        current = data.get("current")

        if current is None:
            raise ValueError(
                "No current weather data returned."
            )

        weather_code = current["weather_code"]

        return CurrentWeatherData(
            temperature=current["temperature_2m"],
            apparent_temperature=current["apparent_temperature"],
            relative_humidity=current["relative_humidity_2m"],
            precipitation=current["precipitation"],
            cloud_cover=current["cloud_cover"],
            wind_speed=current["wind_speed_10m"],
            wind_direction=current["wind_direction_10m"],
            weather_code=weather_code,
            weather_description=WEATHER_CODES.get(weather_code),
        )