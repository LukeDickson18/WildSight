import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Observation(Base):
    __tablename__ = "observations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    species_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("species.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    location_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("locations.id", ondelete="RESTRICT"),
        nullable=True, #Changed from False to True to allow for observations without a location for testing
        index=True,
    )

    weather_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("weather.id", ondelete="SET NULL"),
        nullable=True,
    )
    astronomy_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("astronomy.id", ondelete="SET NULL"),
        nullable=True,
    )

    hotspot_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("hotspots.id", ondelete="SET NULL"),
        nullable=True,
    )

    observation_datetime: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
    )

    count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
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

    user: Mapped["User"] = relationship(
        back_populates="observations",
    )

    species: Mapped["Species"] = relationship(
        back_populates="observations",
    )

    location: Mapped["Location"] = relationship(
        back_populates="observations",
    )

    weather: Mapped["Weather"] = relationship(
        back_populates="observations",
    )

    astronomy: Mapped["Astronomy"] = relationship(
        back_populates="observations",
    )

    hotspot: Mapped["Hotspot"] = relationship(
        back_populates="observations",
    )