from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.base import Base
from models.mixins.int_id_pk import IntIdPkMixin


class Book(Base, IntIdPkMixin):
    """
    Модель книги.
    """

    title: Mapped[str]
    description: Mapped[str | None]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id", ondelete="CASCADE"))
    available_amount: Mapped[int]

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({self.id=}, {self.title=}, {self.description=}, {self.author_id=}, {self.available_amount=})"
        )
