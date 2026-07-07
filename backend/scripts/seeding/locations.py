from sqlalchemy import func, select

from app.db.database import SessionLocal
from app.models.location import Location


LOCATIONS = [
    {
        "name": "Kirstenbosch National Botanical Garden",
        "latitude": -33.9875,
        "longitude": 18.4327,
    },
    {
        "name": "Rondevlei Nature Reserve",
        "latitude": -34.0624,
        "longitude": 18.5020,
    },
    {
        "name": "Table Mountain National Park",
        "latitude": -33.9628,
        "longitude": 18.4098,
    },
    {
        "name": "Strandfontein Sewage Works",
        "latitude": -34.0802,
        "longitude": 18.5654,
    },
    {
        "name": "Jonkershoek Nature Reserve",
        "latitude": -33.9885,
        "longitude": 18.9655,
    },
    {
        "name": "Harold Porter Botanical Garden",
        "latitude": -34.3328,
        "longitude": 18.9134,
    },
    {
        "name": "West Coast National Park",
        "latitude": -33.1808,
        "longitude": 18.0843,
    },
    {
        "name": "Intaka Island",
        "latitude": -33.8905,
        "longitude": 18.5072,
    },
    {
        "name": "Rietvlei Nature Reserve",
        "latitude": -33.8235,
        "longitude": 18.4898,
    },
    {
        "name": "Silvermine Nature Reserve",
        "latitude": -34.0890,
        "longitude": 18.4218,
    },
]


def seed_locations() -> None:
    db = SessionLocal()

    try:
        created = 0
        skipped = 0

        for location_data in LOCATIONS:

            existing = db.scalar(
                select(Location).where(
                    Location.name == location_data["name"]
                )
            )

            if existing:
                skipped += 1
                continue

            point = func.ST_GeomFromText(
                f"POINT({location_data['longitude']} {location_data['latitude']})",
                4326,
            )

            location = Location(
                name=location_data["name"],
                coordinates=point,
            )

            db.add(location)
            created += 1

        db.commit()

        print(f"Created : {created}")
        print(f"Skipped : {skipped}")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_locations()