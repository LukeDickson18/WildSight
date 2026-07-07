from uuid import UUID

from geoalchemy2.functions import ST_DWithin, ST_X, ST_Y
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models import Location


class LocationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, location: Location) -> Location:
        self.db.add(location)
        self.db.commit()
        self.db.refresh(location)
        return location

    def get_by_id(
        self,
        location_id: UUID,
    ) -> Location | None:
        return self.db.get(Location, location_id)

    def get_locations(
        self,
        page: int,
        page_size: int,
    ) -> tuple[list[Location], int]:

        total = self.db.scalar(
            select(func.count()).select_from(Location)
        ) or 0

        locations = self.db.scalars(
            select(Location)
            .order_by(Location.created_at.desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
        ).all()

        return locations, total

    def get_nearby_locations(
        self,
        latitude: float,
        longitude: float,
        radius: int,
        page: int,
        page_size: int,
    ) -> tuple[list[Location], int]:

        point = from_shape(
            Point(longitude, latitude),
            srid=4326,
        )

        filter_clause = ST_DWithin(
            Location.coordinates,
            point,
            radius,
        )

        total = self.db.scalar(
            select(func.count())
            .select_from(Location)
            .where(filter_clause)
        ) or 0

        locations = self.db.scalars(
            select(Location)
            .where(filter_clause)
            .order_by(Location.created_at.desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
        ).all()

        return locations, total

    def get_coordinates(
        self,
        location_id: UUID,
    ) -> tuple[float, float] | None:

        stmt = (
            select(
                ST_Y(Location.coordinates),
                ST_X(Location.coordinates),
            )
            .where(Location.id == location_id)
        )

        result = self.db.execute(stmt).first()

        if result is None:
            return None

        latitude, longitude = result

        return float(latitude), float(longitude)

    def update(
        self,
        location: Location,
    ) -> Location:
        self.db.add(location)
        self.db.commit()
        self.db.refresh(location)
        return location