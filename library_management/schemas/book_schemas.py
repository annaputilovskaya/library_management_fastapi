from pydantic import BaseModel, Field, NonNegativeInt


class BookSchema(BaseModel):
    """
    Базовая схема книга.
    """

    title: str = Field(title="Название", max_length=100)
    description: str | None = None
    author_id: int = Field(title="Автор")
    available_amount: NonNegativeInt | None = None


class BookReadSchema(BookSchema):
    """
    Схема просмотра книги.
    """

    id: int
