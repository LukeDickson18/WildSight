from __future__ import annotations

import uuid

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Species(Base):
    __tablename__ = "species"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    ebird_code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    common_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    scientific_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    wildlife_group: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="Bird",
    )

    family_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("families.id"),
        nullable=False,
        index=True,
    )

    # ---------------------------
    # iNaturalist metadata
    # ---------------------------

    inat_taxon_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
        unique=True,
        index=True,
    )

    image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    thumbnail_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    image_license: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    image_attribution: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    image_source: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
        default="iNaturalist",
    )

    family: Mapped["Family"] = relationship(
        back_populates="species",
    )

    observations: Mapped[list["Observation"]] = relationship(
        back_populates="species",
    )

    countries: Mapped[list["SpeciesCountry"]] = relationship(
        back_populates="species",
        cascade="all, delete-orphan",
    )