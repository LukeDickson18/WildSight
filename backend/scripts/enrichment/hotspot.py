from sqlalchemy import select

from app.db.session import SessionLocal
from app.enrichment.hotspot import get_nearest_hotspot
from app.models.observation import Observation


MAX_DISTANCE = 1000  # metres


def enrich_hotspots():

    db = SessionLocal()

    try:

        observations = db.scalars(
            select(Observation).where(
                Observation.hotspot_id.is_(None)
            )
        ).all()

        linked = 0
        skipped = 0

        for observation in observations:

            if observation.location is None:
                skipped += 1
                continue

            hotspot = get_nearest_hotspot(
                db=db,
                point=observation.location.coordinates,
                max_distance=MAX_DISTANCE,
            )

            if hotspot is None:
                skipped += 1
                continue

            observation.hotspot = hotspot
            linked += 1

        db.commit()

        print(f"Linked  : {linked}")
        print(f"Skipped : {skipped}")

    finally:
        db.close()


if __name__ == "__main__":
    enrich_hotspots()