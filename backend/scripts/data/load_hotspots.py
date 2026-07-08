import csv
from pathlib import Path

from sqlalchemy import func, select

from app.db.session import SessionLocal
from app.models.hotspot import Hotspot

DATA_FILE = Path("data/raw/ebird/hotspots.csv")


def load_hotspots():

    db = SessionLocal()

    try:

        inserted = 0
        updated = 0

        with DATA_FILE.open(newline="", encoding="utf-8") as file:

            reader = csv.reader(file)

            for row in reader:

                ebird_id = row[0].strip()
                latitude = float(row[4])
                longitude = float(row[5])
                name = row[6].strip()

                hotspot = db.scalar(
                    select(Hotspot).where(
                        Hotspot.ebird_id == ebird_id
                    )
                )

                if hotspot is None:

                    hotspot = Hotspot(
                        ebird_id=ebird_id,
                        name=name,
                        source="ebird",
                        latitude=latitude,
                        longitude=longitude,
                    )

                    hotspot.coordinates = func.ST_SetSRID(
                        func.ST_MakePoint(
                            longitude,
                            latitude,
                        ),
                        4326,
                    )

                    db.add(hotspot)
                    inserted += 1

                else:

                    hotspot.name = name
                    hotspot.latitude = latitude
                    hotspot.longitude = longitude
                    hotspot.source = "ebird"

                    hotspot.coordinates = func.ST_SetSRID(
                        func.ST_MakePoint(
                            longitude,
                            latitude,
                        ),
                        4326,
                    )

                    updated += 1

        db.commit()

        print(f"Inserted : {inserted}")
        print(f"Updated  : {updated}")

    finally:
        db.close()


if __name__ == "__main__":
    load_hotspots()