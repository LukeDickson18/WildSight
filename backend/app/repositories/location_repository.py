from sqlalchemy.orm import Session

from app.models.location import Location


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