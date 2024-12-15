from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from crud.book import book_create
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
