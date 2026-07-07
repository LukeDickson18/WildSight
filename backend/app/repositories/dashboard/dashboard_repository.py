from sqlalchemy import distinct, func, select
from sqlalchemy.orm import Session

from app.models.location import Location
from app.models.observation import Observation


class DashboardRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_dashboard_stats(self) -> dict:

        total_observations = self.db.scalar(
            select(func.count()).select_from(Observation)
        ) or 0

        species_seen = self.db.scalar(
            select(
                func.count(
                    distinct(Observation.species_id)
                )
            )
        ) or 0

        hotspots_visited = self.db.scalar(
            select(
                func.count(
                    distinct(Observation.hotspot_id)
                )
            )
            .where(
                Observation.hotspot_id.is_not(None)
            )
        ) or 0

        countries_visited = self.db.scalar(
            select(
                func.count(
                    distinct(Location.country)
                )
            )
            .join(
                Observation,
                Observation.location_id == Location.id,
            )
            .where(
                Location.country.is_not(None)
            )
        ) or 0

        return {
            "total_observations": total_observations,
            "species_seen": species_seen,
            "hotspots_visited": hotspots_visited,
            "countries_visited": countries_visited,
        }