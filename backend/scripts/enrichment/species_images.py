from sqlalchemy import select

from app.db.session import SessionLocal
from app.enrichment.inaturalist import INaturalistClient
from app.models.country import Country
from app.models.species import Species
from app.models.species_country import SpeciesCountry

BATCH_SIZE = 100

COUNTRIES = [
    "ZA",  # South Africa
    "BW",  # Botswana
    "NA",  # Namibia
    "ZW",  # Zimbabwe
    "MZ",  # Mozambique
    "LS",  # Lesotho
    "SZ",  # Eswatini
]


def enrich_species_images() -> None:
    db = SessionLocal()
    client = INaturalistClient()

    try:
        species_list = db.scalars(
            select(Species)
            .join(SpeciesCountry)
            .join(Country)
            .where(Country.iso_code.in_(COUNTRIES))
            .order_by(Species.common_name)
        ).all()

        total = len(species_list)

        updated = 0
        skipped = 0
        missing = 0

        print(f"Found {total} Southern African species.")

        for index, species in enumerate(species_list, start=1):

            print(
                f"[{index}/{total}] "
                f"{species.common_name} "
                f"({species.scientific_name})",
                end=" ... ",
                flush=True,
            )

            if species.image_url:
                skipped += 1
                print("already imported")
                continue

            image = client.get_species_photo(
                scientific_name=species.scientific_name,
                common_name=species.common_name,
            )

            if image is None:
                missing += 1
                print("no Creative Commons image")
                continue

            species.inat_taxon_id = image["inat_taxon_id"]
            species.image_url = image["image_url"]
            species.thumbnail_url = image["thumbnail_url"]
            species.image_license = image["image_license"]
            species.image_attribution = image["image_attribution"]
            species.image_source = image["image_source"]

            updated += 1

            print(
                f"✓ {image['image_license']}"
            )

            if updated % BATCH_SIZE == 0:
                db.commit()

                print(
                    f"\nCommitted {updated} species "
                    f"({skipped} skipped, {missing} missing).\n"
                )

        db.commit()

        print("\nImport complete.")
        print(f"Updated : {updated}")
        print(f"Skipped : {skipped}")
        print(f"Missing : {missing}")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    enrich_species_images()