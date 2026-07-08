from .auth import router as auth_router
from .dashboard import router as dashboard_router
from .health import router as health_router
from .hotspots import router as hotspot_router
from .observations import router as observation_router
from .species import router as species_router
from .locations import router as location_router
from .users import router as user_router
from .weather import router as weather_router

__all__ = [
    "auth_router",
    "dashboard_router",
    "health_router",
    "hotspot_router",
    "observation_router",
    "species_router",
    "location_router",
    "user_router",
    "weather_router",
]