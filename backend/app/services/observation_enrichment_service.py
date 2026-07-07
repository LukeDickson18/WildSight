from sqlalchemy.orm import Session

from app.models.observation import Observation
from app.repositories.location_repository import LocationRepository
from app.repositories.weather_repository import WeatherRepository
from app.services.weather import WeatherService


class ObservationEnrichmentService:
    """
    Enriches observations with external environmental data.
    """

    def __init__(self, db: Session):
        self.db = db

        self.location_repository = LocationRepository(db)
        self.weather_repository = WeatherRepository(db)
        self.weather_service = WeatherService()

    def enrich_observation(
        self,
        observation: Observation,
    ) -> Observation:
        """
        Enrich a single observation with weather data.
        """

        if observation.weather_id is not None:
            return observation

        if observation.location_id is None:
            return observation

        coordinates = self.location_repository.get_coordinates(
            observation.location_id
        )

        if coordinates is None:
            return observation

        latitude, longitude = coordinates

        weather_data = self.weather_service.get_weather(
            latitude=latitude,
            longitude=longitude,
            observation_datetime=observation.observation_datetime,
        )

        weather = self.weather_repository.get_or_create(
            weather_data
        )

        observation.weather_id = weather.id

        self.db.commit()
        self.db.refresh(observation)

        return observation

    def enrich_all(self) -> int:
        """
        Enrich every observation missing weather.
        """

        observations = (
            self.db.query(Observation)
            .filter(Observation.weather_id.is_(None))
            .all()
        )

        enriched = 0

        for observation in observations:
            self.enrich_observation(observation)
            enriched += 1

        return enriched