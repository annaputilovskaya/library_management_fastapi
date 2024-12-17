from sqlalchemy.orm import Mapped, mapped_column


class IntIdPkMixin:
    """
    Миксин, добавляющий колонку с целочисленным первичным ключом.
    """
    id: Mapped[int] = mapped_column(primary_key=True)
