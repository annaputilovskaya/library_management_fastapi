from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from crud.author import auther_create
from schemas.author_schemas import AuthorReadSchema, AuthorSchema

router = APIRouter(
    prefix="/authors",
    tags=["Авторы"],
)


@router.post(
    "",
    summary="Создание автора",
    response_model=AuthorReadSchema,
    status_code=status.HTTP_201_CREATED,
)
async def add_author(
    author: AuthorSchema,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await auther_create(session=session, author=author)
