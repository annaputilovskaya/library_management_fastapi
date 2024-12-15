from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from crud.borrow import borrow_create, get_borrow_list
from schemas.borrow_schemas import UnfinishedBorrowSchema, BorrowSchema, FinishedBorrowSchema, BorrowReadSchema

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

