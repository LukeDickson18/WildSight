from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.country import Country
from app.models.species import Species
from app.models.species_country import SpeciesCountry
from backend.app.enrichment.ebird import EBirdClient

# --------------------------------------------------
# Countries to load
# --------------------------------------------------

COUNTRIES = [
    "ZA",
]

client = EBirdClient()


def load_country(session: Session, country_code: str) -> None:
    """
    Load species distribution data for a single country.
    """

    country = session.scalar(
        select(Country).where(
            Country.iso_code == country_code
        )
    )

    if country is None:
        raise ValueError(f"Country '{country_code}' not found.")

    species_codes = client.get_species_codes(country_code)

    inserted = 0
    skipped = 0

    for code in species_codes:

        species = session.scalar(
            select(Species).where(
                Species.ebird_code == code
            )
        )

        if species is None:
            skipped += 1
            continue

        existing = session.scalar(
            select(SpeciesCountry).where(
                SpeciesCountry.species_id == species.id,
                SpeciesCountry.country_id == country.id,
            )
        )

        if existing:
            continue

        session.add(
            SpeciesCountry(
                species_id=species.id,
                country_id=country.id,
            )
        )

        inserted += 1

    session.commit()

    print(
        f"{country_code}: "
        f"{inserted} species linked "
        f"({skipped} not found in taxonomy)"
    )


def main() -> None:
    session: Session = SessionLocal()

    try:
        for country_code in COUNTRIES:
            load_country(session, country_code)

    finally:
        session.close()


if __name__ == "__main__":
    main()