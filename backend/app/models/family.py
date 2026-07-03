import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Family(Base):
    __tablename__ = "families"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    family_code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    common_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    scientific_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    order_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("orders.id"),
        nullable=False,
    )

    order: Mapped["Order"] = relationship(
        back_populates="families",
    )

    species: Mapped[list["Species"]] = relationship(
        back_populates="family",
    )