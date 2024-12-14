"""unique constraint for author

Revision ID: 240bf0aa5882
Revises: 0f08e305d898
Create Date: 2024-12-14 16:31:16.640891

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "240bf0aa5882"
down_revision: Union[str, None] = "0f08e305d898"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(
        op.f("uq_author_first_name_last_name_born_at"),
        "author",
        ["first_name", "last_name", "born_at"],
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("uq_author_first_name_last_name_born_at"),
        "author",
        type_="unique",
    )
