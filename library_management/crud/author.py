from fastapi import HTTPException, status
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
