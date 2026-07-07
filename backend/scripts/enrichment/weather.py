from __future__ import annotations

from geoalchemy2.shape import to_shape
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.db.session import SessionLocal
from app.models.observation import Observation
from app.repositories.weather_repository import WeatherRepository
from app.enrichment.weather import WeatherService

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

        for index, observation in enumerate(observations, start=1):

            if observation.location is None:
                continue

            point = to_shape(observation.location.coordinates)

            longitude = point.x
            latitude = point.y

            try:
                weather_data = weather_service.get_weather(
                    latitude=latitude,
                    longitude=longitude,
                    observation_datetime=observation.observation_datetime,
                )

                weather = weather_repository.get_or_create(
                    weather_data
                )

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