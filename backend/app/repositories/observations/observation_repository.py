from __future__ import annotations

from datetime import date, datetime, time
from uuid import UUID

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, joinedload

from app.models.location import Location
from app.models.observation import Observation
from app.models.species import Species


class ObservationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        observation: Observation,
    ) -> Observation:
        self.db.add(observation)
        self.db.commit()
        self.db.refresh(observation)
        return observation

    def get_by_id(
        self,
        observation_id: UUID,
    ) -> Observation | None:
        stmt = (
            select(Observation)
            .options(
                joinedload(Observation.species),
                joinedload(Observation.location),
                joinedload(Observation.weather),
                joinedload(Observation.hotspot),
                joinedload(Observation.user),
            )
            .where(Observation.id == observation_id)
        )

        return self.db.scalar(stmt)

    def get_observations(
        self,
        *,
        user_id: UUID,
        page: int,
        page_size: int,
        search: str | None = None,
        species_id: UUID | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
        sort: str = "newest",
    ) -> tuple[list[Observation], int]:

        stmt = (
            select(Observation)
            .join(Observation.species)
            .outerjoin(Observation.location)
            .options(
                joinedload(Observation.species),
                joinedload(Observation.location),
                joinedload(Observation.weather),
                joinedload(Observation.hotspot),
                joinedload(Observation.user),
            )
            .where(Observation.user_id == user_id)
        )

        #
        # Search
        #
        if search:
            search_term = f"%{search.strip()}%"

            stmt = stmt.where(
                or_(
                    Species.common_name.ilike(search_term),
                    Species.scientific_name.ilike(search_term),
                    Observation.notes.ilike(search_term),
                    Location.name.ilike(search_term),
                )
            )

        #
        # Species filter
        #
        if species_id:
            stmt = stmt.where(
                Observation.species_id == species_id
            )

        #
        # Date filters
        #
        if start_date:
            stmt = stmt.where(
                Observation.observation_datetime
                >= datetime.combine(
                    start_date,
                    time.min,
                )
            )

        if end_date:
            stmt = stmt.where(
                Observation.observation_datetime
                <= datetime.combine(
                    end_date,
                    time.max,
                )
            )

        #
        # Count BEFORE pagination
        #
        total = self.db.scalar(
            select(func.count())
            .select_from(stmt.subquery())
        )

        #
        # Sorting
        #
        match sort:

            case "oldest":
                stmt = stmt.order_by(
                    Observation.observation_datetime.asc()
                )

            case "species":
                stmt = stmt.order_by(
                    Species.common_name.asc(),
                    Observation.observation_datetime.desc(),
                )

            case "updated":
                stmt = stmt.order_by(
                    Observation.updated_at.desc()
                )

            case _:
                stmt = stmt.order_by(
                    Observation.observation_datetime.desc()
                )

        #
        # Pagination
        #
        stmt = (
            stmt.offset((page - 1) * page_size)
            .limit(page_size)
        )

        observations = (
            self.db.scalars(stmt)
            .unique()
            .all()
        )

        return observations, total

    def update(
        self,
        observation: Observation,
    ) -> Observation:
        self.db.commit()
        self.db.refresh(observation)
        return observation

    def delete(
        self,
        observation: Observation,
    ) -> None:
        self.db.delete(observation)
        self.db.commit()