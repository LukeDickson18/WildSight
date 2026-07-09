import uuid

from sqlalchemy import Float, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    common_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    taxon_order: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    families: Mapped[list["Family"]] = relationship(
        back_populates="order",
    )