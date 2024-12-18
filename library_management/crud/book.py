from typing import List

from fastapi import HTTPException, status
from sqlalchemy import select
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


async def get_book_list(
    session: AsyncSession,
) -> List[Book]:
    """
    Получает список книг в алфавитном порядке названий.
    """

    stmt = select(Book).order_by(Book.title)
    books = await session.scalars(stmt)
    return list(books)


async def get_book(session: AsyncSession, book_id: int) -> Book | None:
    """
    Получает книгу по ее идентификатору.
    """

    return await session.scalar(select(Book).where(Book.id == book_id))


async def book_update(session: AsyncSession, book_in: BookSchema, book: Book) -> Book:
    """
    Обновляет информацию о книге.
    """

    book_dict = book_in.model_dump()
    for name, value in book_dict.items():
        setattr(book, name, value)

    try:
        await session.commit()
        return book
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": f"Book already exists or author {book.author_id} not found!"
            },
        )


async def book_delete(session: AsyncSession, book: Book) -> dict[str, str]:
    """
    Удаляет книгу.
    """

    await session.delete(book)
    await session.commit()
    return {"detail": "Book deleted."}
