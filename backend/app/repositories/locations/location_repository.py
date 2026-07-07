from app.models import Location 
from sqlalchemy.orm import Session
from sqlalchemy import select
from geoalchemy2.functions import ST_X, ST_Y


class LocationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, location: Location) -> Location:
        self.db.add(location)
        self.db.commit()
        self.db.refresh(location)
        return location

    def get(self, location_id):
        return self.db.get(Location, location_id)
    
    def get_coordinates(
            self, 
            location_id
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
    
    def update(self, location: Location) -> Location:
        self.db.add(location)
        self.db.commit()
        self.db.refresh(location)
        return location