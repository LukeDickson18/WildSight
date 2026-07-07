from sqlalchemy import or_, select

from app.core.settings import settings
from app.db.session import SessionLocal
from app.enrichment.hotspot import get_nearest_hotspot
from app.models.observation import Observation

MAX_DISTANCE = settings.hotspot_link_distance_m


def enrich_hotspots():

    db = SessionLocal()

    try:

        observations = db.scalars(
            select(Observation).where(
                or_(
                    Observation.hotspot_id.is_(None),
                    Observation.distance_to_hotspot_m.is_(None),
                )
            )
        ).all()

        linked = 0
        skipped = 0

        for observation in observations:

            if observation.location is None:
                print(f"{observation.id}: location is None")
                skipped += 1
                continue

            hotspot, distance = get_nearest_hotspot(
                db=db,
                point=observation.location.coordinates,
            )

            if hotspot is None or distance is None:
                print(f"{observation.id}: no hotspot found")
                skipped += 1
                continue

            # Always store the distance to the nearest hotspot
            observation.distance_to_hotspot_m = distance

            if distance > MAX_DISTANCE:
                print(
                    f"{observation.id}: nearest hotspot "
                    f"{hotspot.name} ({distance:.0f} m away)"
                )
                skipped += 1
                continue

            # Only relink if necessary
            if observation.hotspot_id is None:
                observation.hotspot = hotspot
                linked += 1

                print(
                    f"{observation.id}: linked to "
                    f"{hotspot.name} ({distance:.0f} m)"
                )

        db.commit()

        print(f"Linked  : {linked}")
        print(f"Outside Range : {skipped}")

    finally:
        db.close()


if __name__ == "__main__":
    enrich_hotspots()