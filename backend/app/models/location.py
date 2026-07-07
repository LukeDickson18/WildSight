import uuid
from datetime import datetime

from geoalchemy2 import Geometry
from sqlalchemy import DateTime, Float, String, func
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

    # Optional user-friendly name
    name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True,
    )

    # Reverse geocoded information
    country: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    state_province: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    municipality: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    locality: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    # Derived environmental information
    elevation: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    biome: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    habitat: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    protected_area: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    # PostGIS geometry (POINT in WGS84)
    coordinates: Mapped[object] = mapped_column(
        Geometry(
            geometry_type="POINT",
            srid=4326,
            spatial_index=True,
        ),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    observations: Mapped[list["Observation"]] = relationship(
        back_populates="location",
    )