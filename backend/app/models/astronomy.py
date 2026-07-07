import uuid
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Astronomy(Base):
    __tablename__ = "astronomy"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    sunrise: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    sunset: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    day_length: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    season: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    moon_phase: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    moon_illumination: Mapped[float | None] = mapped_column(
        Float,
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

    observations: Mapped[list["Observation"]] = relationship(
        back_populates="astronomy",
    )