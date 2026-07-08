from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth import router as auth_router
from app.routers.health import router as health_router
from app.routers.species import router as species_router
from app.core.settings import settings
from app.routers.observations import router as observations_router
from app.routers.dashboard import router as dashboard_router
from app.routers.weather import router as weather_router

app = FastAPI(
    title="WildSight API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(auth_router)
app.include_router(health_router)
app.include_router(species_router)
app.include_router(observations_router)
app.include_router(dashboard_router)
app.include_router(weather_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to the WildSight API!"
    }