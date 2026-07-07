from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session, joinedload

from app.models.observation import Observation


class ObservationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, observation: Observation) -> Observation:
        self.db.add(observation)
        self.db.commit()
        self.db.refresh(observation)
        return observation

    def get_by_id(self, observation_id: UUID) -> Observation | None:
        stmt = (
            select(Observation)
            .options(
                joinedload(Observation.species),
                joinedload(Observation.location),
                joinedload(Observation.weather),   # NEW
                joinedload(Observation.user),
            )
            .where(Observation.id == observation_id)
        )

        return self.db.scalar(stmt)

    def get_observations(
        self,
        page: int,
        page_size: int,
    ) -> tuple[list[Observation], int]:
        total = self.db.scalar(
            select(func.count()).select_from(Observation)
        )

        stmt = (
            select(Observation)
            .options(
                joinedload(Observation.species),
                joinedload(Observation.location),
                joinedload(Observation.weather),   # NEW
                joinedload(Observation.user),
            )
            .order_by(Observation.observation_datetime.desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
        )

        observations = self.db.scalars(stmt).all()

        return observations, total

    def update(self, observation: Observation) -> Observation:
        self.db.commit()
        self.db.refresh(observation)
        return observation

    def delete(self, observation: Observation) -> None:
        self.db.delete(observation)
        self.db.commit()