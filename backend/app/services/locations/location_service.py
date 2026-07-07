from uuid import UUID

from fastapi import HTTPException, status
from geoalchemy2.elements import WKTElement

from app.models.location import Location
from app.repositories.locations import LocationRepository
from app.schemas.locations.location import (
    LocationCreate,
    LocationListResponse,
    LocationResponse,
)


class LocationService:
    def __init__(
        self,
        repository: LocationRepository,
    ):
        self.repository = repository

    def create_location(
        self,
        data: LocationCreate,
    ) -> Location:

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

    def get_locations(
        self,
        page: int,
        page_size: int,
    ) -> LocationListResponse:

        locations, total = self.repository.get_locations(
            page=page,
            page_size=page_size,
        )

        return LocationListResponse(
            items=locations,
            total=total,
            page=page,
            page_size=page_size,
        )

    def get_location_by_id(
        self,
        location_id: UUID,
    ) -> LocationResponse:

        location = self.repository.get_by_id(
            location_id,
        )

        if location is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Location not found.",
            )

        return location

    def get_nearby_locations(
        self,
        latitude: float,
        longitude: float,
        radius: int,
        page: int,
        page_size: int,
    ) -> LocationListResponse:

        locations, total = self.repository.get_nearby_locations(
            latitude=latitude,
            longitude=longitude,
            radius=radius,
            page=page,
            page_size=page_size,
        )

        return LocationListResponse(
            items=locations,
            total=total,
            page=page,
            page_size=page_size,
        )