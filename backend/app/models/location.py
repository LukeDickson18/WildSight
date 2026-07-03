import uuid

from geoalchemy2 import Geometry
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Location(Base):
    __tablename__ = "locations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    state_province: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    municipality: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    locality: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    coordinates: Mapped[object] = mapped_column(
        Geometry(
            geometry_type="POINT",
            srid=4326,
            spatial_index=True,
        ),
        nullable=False,
    )

    observations: Mapped[list["Observation"]] = relationship(
        back_populates="location",
    )