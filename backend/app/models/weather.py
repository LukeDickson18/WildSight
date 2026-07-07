import uuid
from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Weather(Base):
    __tablename__ = "weather"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # Timestamp of the weather observation
    observation_datetime: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
    )

    # Temperature
    temperature: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    apparent_temperature: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    # Humidity
    relative_humidity: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    dew_point: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    # Atmospheric conditions
    pressure: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    cloud_cover: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    visibility: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    uv_index: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    # Wind
    wind_speed: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    wind_direction: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    wind_gust: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    # Rain
    precipitation: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    # Weather classification
    weather_code: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    weather_description: Mapped[str | None] = mapped_column(
        String(100),
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
        back_populates="weather",
    )