from uuid import UUID

from geoalchemy2.functions import ST_DWithin
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.hotspot import Hotspot


class HotspotRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_hotspots(
        self,
        page: int,
        page_size: int,
    ) -> tuple[list[Hotspot], int]:

        total = self.db.scalar(
            select(func.count()).select_from(Hotspot)
        )

        hotspots = self.db.scalars(
            select(Hotspot)
            .order_by(Hotspot.name)
            .offset((page - 1) * page_size)
            .limit(page_size)
        ).all()

        return hotspots, total

    def get_hotspot_by_id(
        self,
        hotspot_id: UUID,
    ) -> Hotspot | None:

        return self.db.scalar(
            select(Hotspot).where(
                Hotspot.id == hotspot_id
            )
        )

    def get_nearby_hotspots(
        self,
        latitude: float,
        longitude: float,
        radius: int,
        page: int,
        page_size: int,
    ) -> tuple[list[Hotspot], int]:

        point = from_shape(
            Point(longitude, latitude),
            srid=4326,
        )

        filter_clause = ST_DWithin(
            Hotspot.coordinates,
            point,
            radius,
        )

        total = self.db.scalar(
            select(func.count())
            .select_from(Hotspot)
            .where(filter_clause)
        )

        hotspots = self.db.scalars(
            select(Hotspot)
            .where(filter_clause)
            .order_by(Hotspot.name)
            .offset((page - 1) * page_size)
            .limit(page_size)
        ).all()

        return hotspots, total