import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class SpeciesCountry(Base):
    __tablename__ = "species_countries"

    species_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("species.id"),
        primary_key=True,
    )

    country_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("countries.id"),
        primary_key=True,
    )

    species = relationship(
        "Species",
        back_populates="countries",
    )

    country = relationship(
        "Country",
        back_populates="species",
    )