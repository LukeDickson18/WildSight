from pydantic import BaseModel


class DashboardResponse(BaseModel):
    """
    Dashboard statistics displayed at the top of the page.
    """

    total_observations: int
    species_seen: int
    hotspots_visited: int
    countries_visited: int