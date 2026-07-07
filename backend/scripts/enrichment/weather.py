from __future__ import annotations

from geoalchemy2.shape import to_shape
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.db.session import SessionLocal
from app.enrichment.weather import WeatherService
from app.models.observation import Observation
from backend.app.repositories.weather.weather_repository import WeatherRepository

BATCH_SIZE = 100


def enrich_observations() -> None:
    db = SessionLocal()

    weather_service = WeatherService()
    weather_repository = WeatherRepository(db)

    try:
        observations = db.scalars(
            select(Observation)
            .options(
                selectinload(Observation.location),
                selectinload(Observation.weather),
            )
            .where(Observation.weather_id.is_(None))
        ).all()

        enriched = 0

        # Cache weather records by (latitude, longitude, hour)
        weather_cache = {}

        for index, observation in enumerate(observations, start=1):

            if observation.location is None:
                continue

            point = to_shape(observation.location.coordinates)

            latitude = point.y
            longitude = point.x

            observation_hour = observation.observation_datetime.replace(
                minute=0,
                second=0,
                microsecond=0,
            )

            cache_key = (
                round(latitude, 5),
                round(longitude, 5),
                observation_hour,
            )

            try:

                if cache_key in weather_cache:
                    weather = weather_cache[cache_key]

                else:
                    weather_data = weather_service.get_weather(
                        latitude=latitude,
                        longitude=longitude,
                        observation_datetime=observation.observation_datetime,
                    )

                    weather = weather_repository.get_or_create(
                        weather_data
                    )

                    weather_cache[cache_key] = weather

                observation.weather = weather
                enriched += 1

            except Exception as exc:
                print(
                    f"Failed to enrich observation "
                    f"{observation.id}: {exc}"
                )

            if index % BATCH_SIZE == 0:
                db.commit()

        db.commit()

        print(
            f"Successfully enriched {enriched} observations."
        )

    finally:
        db.close()


if __name__ == "__main__":
    enrich_observations()