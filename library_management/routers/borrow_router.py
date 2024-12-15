from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from crud.borrow import borrow_create
from schemas.borrow_schemas import UnfinishedBorrowSchema, BorrowSchema

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
