from typing import List

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models.author_model import Author
from schemas.author_schemas import AuthorSchema


async def auther_create(
        session: AsyncSession,
        author: AuthorSchema
) -> Author:
    """
    Создает автора.
    """
    new_author = Author(**author.model_dump())
    session.add(new_author)
    try:
        await session.commit()
        await session.refresh(new_author)
        return new_author
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"message": "Author already exists"},
        )


async def get_auther_list(
        session: AsyncSession,
) -> List[Author]:
    """
    Получает список авторов в алфавитном порядке фамилий.
    """
    stmt = select(Author).order_by(Author.last_name)
    authors = await session.scalars(stmt)
    return list(authors)

