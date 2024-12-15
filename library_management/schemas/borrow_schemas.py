from datetime import date

from pydantic import BaseModel, Field


class BorrowSchema(BaseModel):
    """
    Базовая схема выдачи.
    """

    book_id: int = Field(title="Книга")
    reader: str = Field(title="Читатель", max_length=100)


class UnfinishedBorrowSchema(BorrowSchema):
    """
    Схема незавершенной выдачи.
    """

    id: int
    given_out_at: date = Field(title="Дата выдачи")


class FinishedBorrowSchema(UnfinishedBorrowSchema):
    """
    Схема завершенной выдачи.
    """

    returned_at: date = Field(title= "Дата возврата")
