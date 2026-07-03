from pathlib import Path

import pandas as pd
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.family import Family
from app.models.order import Order
from app.models.species import Species

DATA_FILE = (
    Path(__file__).resolve().parents[2]
    / "app"
    / "data"
    / "processed"
    / "ebird"
    / "species.csv"
)


def load_taxonomy() -> None:
    df = pd.read_csv(DATA_FILE)

    session: Session = SessionLocal()

    try:
        orders = {}
        families = {}

        inserted_orders = 0
        inserted_families = 0
        inserted_species = 0
        updated_species = 0

        # --------------------------------------------------
        # Orders
        # --------------------------------------------------

        for row in (
            df[["order_name", "taxon_order"]]
            .drop_duplicates()
            .sort_values("taxon_order")
            .itertuples(index=False)
        ):

            existing = session.scalar(
                select(Order).where(Order.name == row.order_name)
            )

            if existing:
                orders[row.order_name] = existing
                continue

            order = Order(
                name=row.order_name,
                taxon_order=float(row.taxon_order),
            )

            session.add(order)
            session.flush()

            orders[row.order_name] = order
            inserted_orders += 1

        # --------------------------------------------------
        # Families
        # --------------------------------------------------

        for row in (
            df[
                [
                    "family_code",
                    "family_common_name",
                    "family_scientific_name",
                    "order_name",
                ]
            ]
            .drop_duplicates()
            .itertuples(index=False)
        ):

            existing = session.scalar(
                select(Family).where(
                    Family.family_code == row.family_code
                )
            )

            if existing:
                families[row.family_code] = existing
                continue

            family = Family(
                family_code=row.family_code,
                common_name=row.family_common_name,
                scientific_name=row.family_scientific_name,
                order_id=orders[row.order_name].id,
            )

            session.add(family)
            session.flush()

            families[row.family_code] = family
            inserted_families += 1

        # --------------------------------------------------
        # Species
        # --------------------------------------------------

        for row in df.itertuples(index=False):

            existing = session.scalar(
                select(Species).where(
                    Species.ebird_code == row.ebird_code
                )
            )

            if existing:
                existing.common_name = row.common_name
                existing.scientific_name = row.scientific_name
                existing.category = row.category
                existing.wildlife_group = "Bird"
                existing.family_id = families[row.family_code].id

                updated_species += 1
                continue

            species = Species(
                ebird_code=row.ebird_code,
                common_name=row.common_name,
                scientific_name=row.scientific_name,
                category=row.category,
                wildlife_group="Bird",
                family_id=families[row.family_code].id,
            )

            session.add(species)
            inserted_species += 1

        session.commit()

        print("\nTaxonomy import complete")
        print(f"Orders inserted   : {inserted_orders}")
        print(f"Families inserted : {inserted_families}")
        print(f"Species inserted  : {inserted_species}")
        print(f"Species updated   : {updated_species}")

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()