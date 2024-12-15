from typing import List

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crud.dependencies import book_by_id
from models.borrow_model import Borrow
from schemas.borrow_schemas import BorrowSchema


async def borrow_create(session: AsyncSession, borrow: BorrowSchema) -> Borrow:
    """
    Создает запись о выдаче.
    """

    book = await book_by_id(book_id=borrow.book_id, session=session)

    if book.available_amount > 0:
        book.available_amount -= 1

        new_borrow = Borrow(book_id=borrow.book_id, reader=borrow.reader.title())
        session.add(new_borrow)
        await session.commit()
        await session.refresh(new_borrow)
        return new_borrow

    else:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail={"message": "No books available"},
        )


async def get_borrow_list(
    session: AsyncSession,
) -> List[Borrow]:
    """
    Получает список всех выдач.
    """

    stmt = select(Borrow).order_by(Borrow.id)
    borrows = await session.scalars(stmt)
    return list(borrows)

