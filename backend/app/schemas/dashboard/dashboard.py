from pydantic import BaseModel

from app.schemas.dashboard.weather import DashboardWeatherResponse


class DashboardResponse(BaseModel):
    """
    Response model for the user's dashboard.

    Combines observation statistics with the current weather
    conditions displayed on the dashboard.
    """

    total_observations: int
    species_seen: int
    hotspots_visited: int
    countries_visited: int

    weather: DashboardWeatherResponse