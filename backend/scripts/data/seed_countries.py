from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.country import Country

# --------------------------------------------------
# Southern African countries
# --------------------------------------------------

COUNTRIES = [
    ("ZA", "South Africa"),
    ("BW", "Botswana"),
    ("NA", "Namibia"),
    ("ZW", "Zimbabwe"),
    ("MZ", "Mozambique"),
    ("LS", "Lesotho"),
    ("SZ", "Eswatini"),
]


def main() -> None:
    session: Session = SessionLocal()

    inserted = 0

    try:
        for iso_code, name in COUNTRIES:

            existing = session.scalar(
                select(Country).where(
                    Country.iso_code == iso_code
                )
            )

            if existing:
                continue

            session.add(
                Country(
                    iso_code=iso_code,
                    name=name,
                )
            )

            inserted += 1

        session.commit()

        print(f"Inserted {inserted} countries.")

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()