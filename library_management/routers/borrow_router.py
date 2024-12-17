from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from crud.borrow import (borrow_create, borrow_update, get_borrow_by_id,
                         get_borrow_list)
from models.borrow_model import Borrow
from schemas.borrow_schemas import (BorrowReadSchema, BorrowSchema,
                                    FinishedBorrowSchema,
                                    UnfinishedBorrowSchema)

router = APIRouter(
    prefix="/borrows",
    tags=["Выдачи"],
)


@router.post(
    "",
    summary="Создание записи о выдаче книги",
    response_model=UnfinishedBorrowSchema,
    status_code=status.HTTP_201_CREATED,
)
async def add_borrow(
    borrow: BorrowSchema,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await borrow_create(borrow=borrow, session=session)


@router.get("", summary="Список всех выдач", response_model=list[BorrowReadSchema])
async def get_all_borrows(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await get_borrow_list(session=session)


@router.get(
    "/{borrow_id}",
    summary="Информация о выдаче по id",
    response_model=BorrowReadSchema,
)
async def get_borrow(borrow: Borrow = Depends(get_borrow_by_id)):
    return borrow


@router.patch(
    "/{borrow_id}/return",
    summary="Завершение выдачи (возврат книги)",
    response_model=FinishedBorrowSchema,
)
async def update_borrow(
    borrow: Borrow = Depends(get_borrow_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await borrow_update(session=session, borrow=borrow)
