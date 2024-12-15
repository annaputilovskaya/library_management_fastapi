from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.base import Base
from models.mixins.int_id_pk import IntIdPkMixin


class Book(Base, IntIdPkMixin):
    """
    Модель книги.
    """

    title: Mapped[str]
    description: Mapped[str | None]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id", ondelete="CASCADE"))
    available_amount: Mapped[int] = mapped_column(default=1)

    author: Mapped["Author"] = relationship(back_populates="books")

    __table_args__ = (UniqueConstraint("title", "author_id"),)

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({self.id=}, {self.title=}, {self.description=}, {self.author_id=}, {self.available_amount=})"
        )
