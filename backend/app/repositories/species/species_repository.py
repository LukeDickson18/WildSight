from uuid import UUID

from geoalchemy2.functions import ST_DWithin
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, selectinload

from app.models.country import Country
from app.models.family import Family
from app.models.location import Location
from app.models.observation import Observation
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
    def __init__(
        self,
        db: Session,
    ):
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

        query = self._apply_search_filter(
            query,
            filters,
        )

        query = self._apply_taxonomy_filters(
            query,
            filters,
        )

        query = self._apply_country_filter(
            query,
            filters,
        )

        query = self._apply_location_filter(
            query,
            filters,
        )

        query = self._apply_hotspot_filter(
            query,
            filters,
        )

        total = self._build_count_query(query)

        query = self._apply_sorting(query)

        query = self._apply_pagination(
            query,
            filters,
        )

        species = self.db.scalars(query).all()

        return SpeciesExplorerResponse(
            items=[
                self._to_species_response(bird)
                for bird in species
            ],
            total=total,
            page=filters.page,
            page_size=filters.page_size,
        )

    #
    # ------------------------------------------------------------------
    # Query Builders
    # ------------------------------------------------------------------
    #

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

    def _build_count_query(
        self,
        query,
    ) -> int:
        return (
            self.db.scalar(
                select(func.count()).select_from(
                    query.subquery()
                )
            )
            or 0
        )

    #
    # ------------------------------------------------------------------
    # Filters
    # ------------------------------------------------------------------
    #

    def _apply_search_filter(
        self,
        query,
        filters: SpeciesExplorerFilters,
    ):
        if not filters.search:
            return query

        return query.where(
            or_(
                Species.common_name.ilike(
                    f"%{filters.search}%"
                ),
                Species.scientific_name.ilike(
                    f"%{filters.search}%"
                ),
                Species.ebird_code.ilike(
                    f"%{filters.search}%"
                ),
            )
        )

    def _apply_taxonomy_filters(
        self,
        query,
        filters: SpeciesExplorerFilters,
    ):
        if filters.order_id:
            query = query.where(
                Order.id == filters.order_id,
            )

        if filters.family_id:
            query = query.where(
                Family.id == filters.family_id,
            )

        return query

    def _apply_country_filter(
        self,
        query,
        filters: SpeciesExplorerFilters,
    ):
        if filters.country_id:
            query = query.where(
                Country.id == filters.country_id,
            )

        return query

    def _apply_location_filter(
        self,
        query,
        filters: SpeciesExplorerFilters,
    ):
        """
        Placeholder for future PostGIS filtering.

        This will eventually:
            Species
                -> Observation
                -> Location

        and use ST_DWithin() to return only species
        observed within the requested radius.
        """

        return query

    def _apply_hotspot_filter(
        self,
        query,
        filters: SpeciesExplorerFilters,
    ):
        """
        Placeholder for future hotspot filtering.

        Will join through Observation and filter
        by Observation.hotspot_id.
        """

        return query
    #
    # ------------------------------------------------------------------
    # Query Helpers
    # ------------------------------------------------------------------
    #

    def _apply_sorting(
        self,
        query,
    ):
        """
        Apply the default ordering for the Species Explorer.
        """

        return query.order_by(
            Order.taxon_order,
            Species.common_name,
        )

    def _apply_pagination(
        self,
        query,
        filters: SpeciesExplorerFilters,
    ):
        """
        Apply pagination to the query.
        """

        return (
            query.offset(
                (filters.page - 1) * filters.page_size
            )
            .limit(filters.page_size)
        )

    #
    # ------------------------------------------------------------------
    # Response Mapping
    # ------------------------------------------------------------------
    #

    @staticmethod
    def _to_species_response(
        species: Species,
    ) -> SpeciesExplorerSpecies:
        """
        Convert a Species ORM model into the API response model.
        """

        return SpeciesExplorerSpecies(
            id=species.id,
            common_name=species.common_name,
            scientific_name=species.scientific_name,
            image_url=species.image_url,
            thumbnail_url=species.thumbnail_url,
            family_common_name=species.family.common_name,
            order_common_name=(
                species.family.order.common_name
                or species.family.order.name
            ),
        )