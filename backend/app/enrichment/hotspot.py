from geoalchemy2 import Geography
from geoalchemy2.functions import ST_DWithin, ST_Distance
from sqlalchemy import select

from app.models.hotspot import Hotspot


def get_nearest_hotspot(db, point, max_distance: float = 1000):
    """
    Return the nearest hotspot within max_distance (metres).

    Parameters
    ----------
    db
        SQLAlchemy session.

    point
        PostGIS POINT geometry.

    max_distance
        Maximum search distance in metres.

    Returns
    -------
    Hotspot | None
    """

    return db.scalar(
        select(Hotspot)
        .where(
            ST_DWithin(
                Geography(Hotspot.coordinates),
                Geography(point),
                max_distance,
            )
        )
        .order_by(
            ST_Distance(
                Geography(Hotspot.coordinates),
                Geography(point),
            )
        )
        .limit(1)
    )