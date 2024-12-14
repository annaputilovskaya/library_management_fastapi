from datetime import date
from typing import Set

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, relationship

from core.base import Base
from models.mixins.int_id_pk import IntIdPkMixin


class Author(Base, IntIdPkMixin):
    """
    Модель автора.
    """

    first_name: Mapped[str]
    last_name: Mapped[str]
    born_at: Mapped[date]

    books: Mapped[Set["Book"]] = relationship(back_populates="author")

    __table_args__ = (UniqueConstraint("first_name", "last_name", "born_at" ),)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id=}, {self.first_name=}, {self.last_name=}, {self.born_at=})"
