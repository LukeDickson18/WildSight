from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.weather import Weather
from app.schemas.weather.weather import WeatherData


class WeatherRepository:
    """
    Repository responsible for all Weather database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_by_datetime(
        self,
        observation_datetime: datetime,
    ) -> Weather | None:
        """
        Retrieve a weather record for a specific observation time.
        """

        stmt = (
            select(Weather)
            .where(
                Weather.observation_datetime == observation_datetime
            )
        )

        return self.db.scalar(stmt)

    def create(
        self,
        weather: WeatherData,
    ) -> Weather:
        """
        Create and persist a new Weather record.
        """

        db_weather = Weather(
            observation_datetime=weather.observation_datetime,
            temperature=weather.temperature,
            apparent_temperature=weather.apparent_temperature,
            relative_humidity=weather.relative_humidity,
            dew_point=weather.dew_point,
            pressure=weather.pressure,
            cloud_cover=weather.cloud_cover,
            visibility=weather.visibility,
            uv_index=weather.uv_index,
            wind_speed=weather.wind_speed,
            wind_direction=weather.wind_direction,
            wind_gust=weather.wind_gust,
            precipitation=weather.precipitation,
            weather_code=weather.weather_code,
            weather_description=weather.weather_description,
        )

        self.db.add(db_weather)
        self.db.commit()
        self.db.refresh(db_weather)

        return db_weather

    def get_or_create(
        self,
        weather: WeatherData,
    ) -> Weather:
        """
        Return an existing weather record if one already exists for the
        observation datetime; otherwise create it.
        """

        existing = self.get_by_datetime(
            weather.observation_datetime
        )

        if existing:
            return existing

        return self.create(weather)

    def delete(
        self,
        weather: Weather,
    ) -> None:
        """
        Delete a weather record.
        """

        self.db.delete(weather)
        self.db.commit()