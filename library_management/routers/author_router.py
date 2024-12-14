from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from crud import author
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
    return await author.auther_create(session=session, author=author)


@router.get("", summary="Список авторов", response_model=list[AuthorReadSchema])
async def get_all_authors(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await author.get_auther_list(session=session)
