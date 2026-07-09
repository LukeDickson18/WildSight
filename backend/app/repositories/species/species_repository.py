from uuid import UUID

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, selectinload

from app.models.country import Country
from app.models.family import Family
from app.models.order import Order
from app.models.species import Species
from app.models.species_country import SpeciesCountry
from app.schemas.species import (
    SpeciesExplorerFilters,
    SpeciesExplorerResponse,
    SpeciesExplorerSpecies,
)

COUNTRY_CODE = "ZA"


class SpeciesRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(
        self,
        species_id: UUID,
    ) -> Species | None:
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

    def get_species_explorer(
        self,
        filters: SpeciesExplorerFilters,
    ) -> SpeciesExplorerResponse:
        query = self._build_base_query()

        query = self._apply_filters(query, filters)

        total = self.db.scalar(
            select(func.count())
            .select_from(query.subquery())
        )

        query = (
            query
            .order_by(
                Order.taxon_order,
                Species.common_name,
            )
            .offset((filters.page - 1) * filters.page_size)
            .limit(filters.page_size)
        )

        species = self.db.scalars(query).all()

        return SpeciesExplorerResponse(
            items=[
                self._to_species_response(bird)
                for bird in species
            ],
            total=total or 0,
            page=filters.page,
            page_size=filters.page_size,
        )

    def _build_base_query(self):
        return (
            select(Species)
            .join(
                SpeciesCountry,
                Species.id == SpeciesCountry.species_id,
            )
            .join(
                Country,
                Country.id == SpeciesCountry.country_id,
            )
            .join(
                Family,
                Species.family_id == Family.id,
            )
            .join(
                Order,
                Family.order_id == Order.id,
            )
            .options(
                selectinload(Species.family).selectinload(Family.order)
            )
            .where(
                Country.iso_code == COUNTRY_CODE,
            )
        )

    def _apply_filters(
        self,
        query,
        filters: SpeciesExplorerFilters,
    ):
        if filters.search:
            query = query.where(
                or_(
                    Species.common_name.ilike(f"%{filters.search}%"),
                    Species.scientific_name.ilike(f"%{filters.search}%"),
                    Species.ebird_code.ilike(f"%{filters.search}%"),
                )
            )

        if filters.order_id:
            query = query.where(
                Order.id == filters.order_id,
            )

        if filters.family_id:
            query = query.where(
                Family.id == filters.family_id,
            )

        if filters.country_id:
            query = query.where(
                Country.id == filters.country_id,
            )

        #
        # GPS filtering
        #

        if (
            filters.latitude is not None
            and filters.longitude is not None
        ):
            # Implement PostGIS filtering later
            pass

        #
        # Hotspot filtering
        #

        if filters.hotspot_id:
            # Implement hotspot filtering later
            pass

        return query

    @staticmethod
    def _to_species_response(
        bird: Species,
    ) -> SpeciesExplorerSpecies:
        return SpeciesExplorerSpecies(
            id=bird.id,
            common_name=bird.common_name,
            scientific_name=bird.scientific_name,
            image_url=bird.image_url,
            thumbnail_url=bird.thumbnail_url,
            family_common_name=bird.family.common_name,
            order_common_name=(
                bird.family.order.common_name
                or bird.family.order.name
            ),
        )