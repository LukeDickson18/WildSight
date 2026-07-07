"""add elevation metadata

Revision ID: 5cb740c48b7e
Revises: fd4dc1e56da8
Create Date: 2026-07-07 12:38:35.951291

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5cb740c48b7e"
down_revision: Union[str, Sequence[str], None] = "fd4dc1e56da8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "locations",
        sa.Column(
            "elevation_source",
            sa.String(length=100),
            nullable=True,
        ),
    )

    op.add_column(
        "locations",
        sa.Column(
            "elevation_enriched_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column("locations", "elevation_enriched_at")
    op.drop_column("locations", "elevation_source")