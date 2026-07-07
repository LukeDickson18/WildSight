from geoalchemy2.shape import to_shape
from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.astronomy import Astronomy
from app.models.observation import Observation

from app.enrichment.astronomy import get_astronomy


def enrich_astronomy():
    db = SessionLocal()

    try:
        observations = db.scalars(
            select(Observation).where(
                Observation.astronomy_id.is_(None)
            )
        ).all()

        created = 0
        reused = 0
        failed = 0

        for observation in observations:
            if observation.location is None:
                continue

            try:
                point = to_shape(observation.location.coordinates)

                data = get_astronomy(
                    latitude=point.y,
                    longitude=point.x,
                    observation_date=observation.observation_datetime.date(),
                )

                existing = db.scalar(
                    select(Astronomy).where(
                        Astronomy.sunrise == data["sunrise"],
                        Astronomy.sunset == data["sunset"],
                        Astronomy.day_length == data["day_length"],
                        Astronomy.season == data["season"],
                        Astronomy.moon_phase == data["moon_phase"],
                        Astronomy.moon_illumination == data["moon_illumination"],
                    )
                )

                if existing:
                    observation.astronomy = existing
                    reused += 1
                else:
                    astronomy = Astronomy(**data)
                    db.add(astronomy)
                    db.flush()

                    observation.astronomy = astronomy
                    created += 1

            except Exception as e:
                failed += 1
                print(
                    f"Failed to enrich observation "
                    f"{observation.id}: {e}"
                )

        db.commit()

        print(f"Created astronomy records : {created}")
        print(f"Reused astronomy records  : {reused}")
        print(f"Failed enrichments        : {failed}")

    finally:
        db.close()


if __name__ == "__main__":
    enrich_astronomy()