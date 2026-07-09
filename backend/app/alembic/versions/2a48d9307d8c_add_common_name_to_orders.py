"""add common name to orders

Revision ID: 2a48d9307d8c
Revises: 471d94ffbbea
Create Date: 2026-07-08 17:45:35.372117
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2a48d9307d8c"
down_revision: Union[str, Sequence[str], None] = "471d94ffbbea"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "orders",
        sa.Column(
            "common_name",
            sa.String(length=100),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column("orders", "common_name")