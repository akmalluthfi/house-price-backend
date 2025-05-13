"""create houses table

Revision ID: ce250e7873a8
Revises: 565fff8709df
Create Date: 2025-05-12 00:35:45.173301

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ce250e7873a8"
down_revision: Union[str, None] = "565fff8709df"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "houses",
        sa.Column("id", sa.Float, primary_key=True),
        sa.Column("price", sa.Integer, nullable=False),
        sa.Column("bedroom", sa.Integer, nullable=False),
        sa.Column("bathroom", sa.Integer, nullable=False),
        sa.Column("land_area", sa.Integer, nullable=False),
        sa.Column("building_area", sa.Integer, nullable=False),
        sa.Column(
            "location_id", sa.Integer, sa.ForeignKey("locations.id"), nullable=False
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("houses")
