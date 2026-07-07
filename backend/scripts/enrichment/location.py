from sqlalchemy import select

from geoalchemy2.shape import to_shape

from app.db.session import SessionLocal
from app.models.location import Location
from app.enrichment.location import reverse_geocode


def enrich_locations():

    db = SessionLocal()

    locations = db.scalars(
        select(Location).where(
            Location.country.is_(None)
        )
    ).all()

    updated = 0

    for location in locations:

        point = to_shape(location.coordinates)

        data = reverse_geocode(
            latitude=point.y,
            longitude=point.x,
        )

        if not data:
            continue

        location.country = data["country"]
        location.state_province = data["state_province"]
        location.municipality = data["municipality"]
        location.locality = data["locality"]

        updated += 1

    db.commit()

    print(f"Successfully enriched {updated} locations.")


if __name__ == "__main__":
    enrich_locations()