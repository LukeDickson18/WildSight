from geoalchemy2.functions import ST_DistanceSphere
from sqlalchemy import select

from app.models.hotspot import Hotspot


def get_nearest_hotspot(
    db,
    point,
):
    """
    Return the nearest hotspot and its distance (metres).

    Parameters
    ----------
    db
        SQLAlchemy session.

    point
        PostGIS POINT geometry.

    Returns
    -------
    tuple[Hotspot | None, float | None]
    """

    distance = ST_DistanceSphere(
        Hotspot.coordinates,
        point,
    ).label("distance")

    result = db.execute(
        select(
            Hotspot,
            distance,
        )
        .order_by(distance)
        .limit(1)
    ).first()

    if result is None:
        return None, None

    hotspot, distance = result

    return hotspot, float(distance)