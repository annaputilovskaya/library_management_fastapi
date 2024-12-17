from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from crud.author import get_author
from crud.book import get_book
from models.author_model import Author
from models.book_model import Book


async def author_by_id(
    author_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Author:
    """
    Получение автора по его идентификатору.
    """

    author = await get_author(session=session, author_id=author_id)
    if author is not None:
        return author

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author {author_id} not found!",
    )


async def book_by_id(
    book_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Book:
    """
    Получение книги по ее идентификатору.
    """

    book = await get_book(session=session, book_id=book_id)
    if book is not None:
        return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book {book_id} not found!",
    )
