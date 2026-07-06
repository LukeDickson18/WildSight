from uuid import UUID

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, selectinload

from app.models.country import Country
from app.models.family import Family
from app.models.species import Species
from app.models.species_country import SpeciesCountry

COUNTRY_CODE = "ZA"


class SpeciesRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_species(
        self,
        page: int,
        page_size: int,
    ) -> tuple[list[Species], int]:
        """Return a paginated list of South African species."""

        base_query = (
            select(Species)
            .join(
                SpeciesCountry,
                Species.id == SpeciesCountry.species_id,
            )
            .join(
                Country,
                Country.id == SpeciesCountry.country_id,
            )
            .where(Country.iso_code == COUNTRY_CODE)
        )

        total = self.db.scalar(
            select(func.count())
            .select_from(base_query.subquery())
        )

        query = (
            base_query
            .options(
                selectinload(Species.family).selectinload(Family.order)
            )
            .order_by(Species.common_name)
            .offset((page - 1) * page_size)
            .limit(page_size)
        )

        species = self.db.scalars(query).all()

        return species, total or 0

    def get_by_id(
        self,
        species_id: UUID,
    ) -> Species | None:
        """Return a South African species by ID."""

        query = (
            select(Species)
            .join(
                SpeciesCountry,
                Species.id == SpeciesCountry.species_id,
            )
            .join(
                Country,
                Country.id == SpeciesCountry.country_id,
            )
            .options(
                selectinload(Species.family).selectinload(Family.order)
            )
            .where(
                Species.id == species_id,
                Country.iso_code == COUNTRY_CODE,
            )
        )

        return self.db.scalar(query)

    def search(
        self,
        query_text: str,
        page: int,
        page_size: int,
    ) -> tuple[list[Species], int]:
        """Search South African species."""

        filter_clause = or_(
            Species.common_name.ilike(f"%{query_text}%"),
            Species.scientific_name.ilike(f"%{query_text}%"),
            Species.ebird_code.ilike(f"%{query_text}%"),
        )

        base_query = (
            select(Species)
            .join(
                SpeciesCountry,
                Species.id == SpeciesCountry.species_id,
            )
            .join(
                Country,
                Country.id == SpeciesCountry.country_id,
            )
            .where(
                Country.iso_code == COUNTRY_CODE,
                filter_clause,
            )
        )

        total = self.db.scalar(
            select(func.count())
            .select_from(base_query.subquery())
        )

        query = (
            base_query
            .options(
                selectinload(Species.family).selectinload(Family.order)
            )
            .order_by(Species.common_name)
            .offset((page - 1) * page_size)
            .limit(page_size)
        )

        species = self.db.scalars(query).all()

        return species, total or 0