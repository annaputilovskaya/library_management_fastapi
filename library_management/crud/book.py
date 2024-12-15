from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models.book_model import Book
from schemas.book_schemas import BookSchema


async def book_create(session: AsyncSession, book: BookSchema) -> Book:
    """
    Создает книгу.
    """

    new_book = Book(**book.model_dump(exclude_unset=True))
    session.add(new_book)
    try:
        await session.commit()
        await session.refresh(new_book)
        return new_book
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": f"Book already exists or author {book.author_id} not found!"
            },
        )
