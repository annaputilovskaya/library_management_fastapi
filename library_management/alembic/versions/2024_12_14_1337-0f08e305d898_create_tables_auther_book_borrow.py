"""create tables auther, book, borrow

Revision ID: 0f08e305d898
Revises: 
Create Date: 2024-12-14 13:37:58.605623

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0f08e305d898"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "author",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("born_at", sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_author")),
    )
    op.create_table(
        "book",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.Column("available_amount", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["author.id"],
            name=op.f("fk_book_author_id_author"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_book")),
    )
    op.create_table(
        "borrow",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("book_id", sa.Integer(), nullable=False),
        sa.Column("reader", sa.String(), nullable=False),
        sa.Column("given_out_at", sa.Date(), nullable=False),
        sa.Column("returned_at", sa.Date(), nullable=False),
        sa.ForeignKeyConstraint(
            ["book_id"],
            ["book.id"],
            name=op.f("fk_borrow_book_id_book"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_borrow")),
    )


def downgrade() -> None:
    op.drop_table("borrow")
    op.drop_table("book")
    op.drop_table("author")
