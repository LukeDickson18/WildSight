from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_observations: int
    species_seen: int
    hotspots_visited: int
    countries_visited: int