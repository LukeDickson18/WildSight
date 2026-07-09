from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.country import Country
from app.models.order import Order
from app.models.family import Family
from app.models.hotspot import Hotspot


class LookupRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_countries(self):
        query = (
            select(Country)
            .order_by(Country.name)
        )

        return self.db.scalars(query).all()

    def get_orders(self):
        query = (
            select(Order)
            .order_by(Order.taxon_order)
        )

        return self.db.scalars(query).all()

    def get_families(self):
        query = (
            select(Family)
            .order_by(Family.common_name)
        )

        return self.db.scalars(query).all()

    def get_hotspots(self):
        query = (
            select(Hotspot)
            .order_by(Hotspot.name)
        )

        return self.db.scalars(query).all()