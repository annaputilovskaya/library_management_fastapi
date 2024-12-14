from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from crud.author import get_author
from models.author_model import Author


async def author_by_id(
    author_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Author:
    """
    Получение заметки по ее идентификатору.
    """

    author = await get_author(session=session, author_id=author_id)
    if author is not None:
        return author

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author {author_id} not found!",
    )
