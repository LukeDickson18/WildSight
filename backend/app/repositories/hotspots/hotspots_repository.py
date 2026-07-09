from uuid import UUID

from geoalchemy2.functions import ST_DWithin
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

        total = (
            self.db.scalar(
                select(func.count()).select_from(Hotspot)
            )
            or 0
        )

        hotspots = (
            self.db.scalars(
                select(Hotspot)
                .order_by(Hotspot.name)
                .offset((page - 1) * page_size)
                .limit(page_size)
            )
            .all()
        )

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
    ):

        search_point = func.ST_SetSRID(
            func.ST_MakePoint(longitude, latitude),
            4326,
        )

        distance = (
            func.ST_DistanceSphere(
                Hotspot.coordinates,
                search_point,
            )
            / 1000.0
        ).label("distance_km")

        filter_clause = ST_DWithin(
            Hotspot.coordinates,
            search_point,
            radius / 111.32,
        )

        total = (
            self.db.scalar(
                select(func.count())
                .select_from(Hotspot)
                .where(filter_clause)
            )
            or 0
        )

        rows = self.db.execute(
            select(
                Hotspot,
                distance,
            )
            .where(filter_clause)
            .order_by(distance)
            .offset((page - 1) * page_size)
            .limit(page_size)
        ).all()

        return rows, total