from datetime import date

from pydantic import BaseModel, Field


class AuthorSchema(BaseModel):
    """
    Базовая схема автора.
    """

    first_name: str = Field(title="Имя", max_length=50)
    last_name: str = Field(title="Фамилия", max_length=50)
    born_at: date = Field(title="Дата рождения")


class AuthorReadSchema(AuthorSchema):
    """
    Схема просмотра автора.
    """

    id: int
