"""unique constraint for book

Revision ID: 33535b2c08fc
Revises: 240bf0aa5882
Create Date: 2024-12-14 21:22:27.191050

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "33535b2c08fc"
down_revision: Union[str, None] = "240bf0aa5882"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(
        op.f("uq_book_title_author_id"), "book", ["title", "author_id"]
    )


def downgrade() -> None:
    op.drop_constraint(op.f("uq_book_title_author_id"), "book", type_="unique")
