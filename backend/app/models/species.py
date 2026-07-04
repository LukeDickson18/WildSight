import uuid

from sqlalchemy import ForeignKey, String
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
    

    family: Mapped["Family"] = relationship(
        back_populates="species",
    )

    observations: Mapped[list["Observation"]] = relationship(
        back_populates="species",
    )