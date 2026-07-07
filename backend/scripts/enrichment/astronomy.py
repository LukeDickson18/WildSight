from sqlalchemy import select

from app.db.session import SessionLocal

from app.models.astronomy import Astronomy
from app.models.location import Location
from app.models.observation import Observation

from backend.app.enrichment.astronomy import get_astronomy

from geoalchemy2.shape import to_shape


def enrich_astronomy():

    db = SessionLocal()

    observations = db.scalars(
        select(Observation).where(
            Observation.astronomy_id.is_(None)
        )
    ).all()

    created = 0

    for observation in observations:

        if observation.location is None:
            continue

        point = to_shape(observation.location.coordinates)

        data = get_astronomy(
            latitude=point.y,
            longitude=point.x,
            observation_date=observation.observation_datetime.date(),
        )

        astronomy = Astronomy(**data)

        db.add(astronomy)
        db.flush()

        observation.astronomy = astronomy

        created += 1

    db.commit()

    print(f"Successfully enriched {created} observations.")


if __name__ == "__main__":
    enrich()