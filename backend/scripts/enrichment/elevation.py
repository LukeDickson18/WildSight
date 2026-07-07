from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.location import Location
from app.enrichment.elevation import ElevationService
from geoalchemy2.shape import to_shape

BATCH_SIZE = 100


def enrich_locations() -> None:
    db = SessionLocal()

    try:
        locations = db.scalars(
            select(Location).where(Location.elevation.is_(None))
        ).all()

        enriched = 0

        for index, location in enumerate(locations, start=1):
            point = to_shape(location.coordinates)

            longitude = point.x
            latitude = point.y

            elevation = ElevationService.get_elevation(
                latitude,
                longitude,
            )

            if elevation is None:
                continue

            location.elevation = elevation
            location.elevation_source = "Open-Meteo"
            location.elevation_enriched_at = datetime.now(timezone.utc)

            enriched += 1

            if index % BATCH_SIZE == 0:
                db.commit()

        db.commit()

        print(f"Successfully enriched {enriched} locations.")

    finally:
        db.close()


if __name__ == "__main__":
    enrich_locations()