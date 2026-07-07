import random
from datetime import datetime, timedelta, UTC

from sqlalchemy import select

from app.db.database import SessionLocal
from app.models.location import Location
from app.models.observation import Observation
from app.models.species import Species
from app.models.user import User


DEFAULT_NUMBER_OF_OBSERVATIONS = 100

OBSERVATION_NOTES = [
    "Seen feeding in grass.",
    "Calling from nearby trees.",
    "Perched on fence.",
    "Flying overhead.",
    "Foraging with small flock.",
    "Observed near water.",
    "Very active this morning.",
    "Juvenile present.",
    "Pair observed together.",
    None,
]


def random_datetime_last_year() -> datetime:
    now = datetime.now(UTC)
    days = random.randint(0, 365)
    hours = random.randint(5, 18)
    minutes = random.randint(0, 59)

    dt = now - timedelta(days=days)
    return dt.replace(
        hour=hours,
        minute=minutes,
        second=0,
        microsecond=0,
    )


def seed_observations(number_of_observations: int = DEFAULT_NUMBER_OF_OBSERVATIONS) -> None:
    db = SessionLocal()

    try:
        users = db.scalars(select(User)).all()
        species = db.scalars(select(Species)).all()
        locations = db.scalars(select(Location)).all()

        if not users:
            raise ValueError("No users found. Run users.py first.")

        if not species:
            raise ValueError("No species found.")

        if not locations:
            raise ValueError("No locations found.")

        created = 0

        for _ in range(number_of_observations):
            observation = Observation(
                user=random.choice(users),
                species=random.choice(species),
                location=random.choice(locations),
                observation_datetime=random_datetime_last_year(),
                count=random.randint(1, 8),
                notes=random.choice(OBSERVATION_NOTES),
            )

            db.add(observation)
            created += 1

        db.commit()

        print(f"Created observations : {created}")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_observations()