"""add type none to returned_at

Revision ID: bd47e4ed3b66
Revises: 33535b2c08fc
Create Date: 2024-12-15 20:32:58.100889

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bd47e4ed3b66"
down_revision: Union[str, None] = "33535b2c08fc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "borrow", "returned_at", existing_type=sa.DATE(), nullable=True
    )


def downgrade() -> None:
    op.alter_column(
        "borrow", "returned_at", existing_type=sa.DATE(), nullable=False
    )
