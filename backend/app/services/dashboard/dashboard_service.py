from app.repositories.dashboard import DashboardRepository
from app.schemas.dashboard import DashboardResponse


class DashboardService:
    def __init__(
        self,
        repository: DashboardRepository,
    ):
        self.repository = repository

    def get_dashboard(self) -> DashboardResponse:
        stats = self.repository.get_dashboard_stats()

        return DashboardResponse(
            total_observations=stats["total_observations"],
            species_seen=stats["species_seen"],
            hotspots_visited=stats["hotspots_visited"],
            countries_visited=stats["countries_visited"],
        )