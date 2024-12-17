from datetime import date
from typing import Annotated, List

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
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


async def get_borrow_by_id(
    borrow_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Borrow | None:
    """
    Получает информацию о выдаче по ее идентификатору.
    """

    borrow = await session.scalar(select(Borrow).where(Borrow.id == borrow_id))
    if borrow is not None:
        return borrow

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Borrow {borrow_id} not found!",
    )


async def borrow_update(session: AsyncSession, borrow: Borrow) -> Borrow:
    """
    Обновляет информацию о выдаче.
    """

    if not borrow.returned_at:
        book = await book_by_id(book_id=borrow.book_id, session=session)
        book.available_amount += 1
        borrow.returned_at = date.today()

        await session.commit()
        await session.refresh(borrow)
        return borrow

    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"message": "Book already returned"},
        )
