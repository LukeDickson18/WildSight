from geoalchemy2.elements import WKTElement

from app.models.location import Location
from app.repositories.location_repository import LocationRepository
from app.schemas.location import LocationCreate


class LocationService:

    def __init__(self, repository: LocationRepository):
        self.repository = repository

    def create_location(self, data: LocationCreate) -> Location:

        point = WKTElement(
            f"POINT({data.longitude} {data.latitude})",
            srid=4326,
        )

        location = Location(
            name=data.name,
            country=data.country,
            state_province=data.state_province,
            municipality=data.municipality,
            locality=data.locality,
            coordinates=point,
        )

        return self.repository.create(location)