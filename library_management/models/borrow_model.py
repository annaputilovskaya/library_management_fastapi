from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.base import Base
from models.book_model import Book
from models.mixins.int_id_pk import IntIdPkMixin


class Borrow(Base, IntIdPkMixin):
    """
    Модель выдачи.
    """

    book_id: Mapped[int] = mapped_column(ForeignKey("book.id", ondelete="CASCADE"))
    reader: Mapped[str]
    given_out_at: Mapped[date] = mapped_column(default=date.today)
    returned_at: Mapped[date | None] = mapped_column(onupdate=date.today)

    book: Mapped[Book] = relationship()

    def __str__(self):
        return f"{self.reader} - {self.book_id}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({self.id=}, {self.book_id=}, {self.reader=}, {self.given_out_at=}, {self.returned_at=})"
        )
