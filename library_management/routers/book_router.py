from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from crud.book import book_create, book_delete, book_update, get_book_list
from crud.dependencies import book_by_id
from models.book_model import Book
from schemas.book_schemas import BookReadSchema, BookSchema

router = APIRouter(
    prefix="/books",
    tags=["Книги"],
)


@router.post(
    "",
    summary="Создание книги",
    response_model=BookReadSchema,
    status_code=status.HTTP_201_CREATED,
)
async def add_book(
    book: BookSchema,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await book_create(book=book, session=session)


@router.get("", summary="Список книг", response_model=list[BookReadSchema])
async def get_all_books(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await get_book_list(session=session)


@router.get(
    "/{book_id}",
    summary="Информация о книге по id",
    response_model=BookReadSchema,
)
async def get_book(book: Book = Depends(book_by_id)):
    return book


@router.put(
    "/{book_id}",
    summary="Обновление информации о книге",
    response_model=BookReadSchema,
)
async def update_book(
    book_in: BookSchema,
    book: Book = Depends(book_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await book_update(session=session, book=book, book_in=book_in)


@router.delete(
    "/{book_id}", summary="Удаление книги", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book(
    book: Book = Depends(book_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await book_delete(session=session, book=book)
