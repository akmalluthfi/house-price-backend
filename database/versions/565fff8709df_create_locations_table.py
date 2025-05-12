"""create locations table

Revision ID: 565fff8709df
Revises:
Create Date: 2025-05-12 00:21:53.264927

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "565fff8709df"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "locations",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("district", sa.String(50), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("locations")
