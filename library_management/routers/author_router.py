from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from crud.author import (author_create, author_delete, author_update,
                         get_author_list)
from crud.dependencies import author_by_id
from models.author_model import Author
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
    return await author_create(session=session, author=author)


@router.get("", summary="Список авторов", response_model=list[AuthorReadSchema])
async def get_all_authors(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await get_author_list(session=session)


@router.get(
    "/{author_id}",
    summary="Информация об авторе по id",
    response_model=AuthorReadSchema,
)
async def get_author(author: Author = Depends(author_by_id)):
    return author


@router.put(
    "/{author_id}",
    summary="Обновление информации об авторе",
    response_model=AuthorReadSchema,
)
async def update_author(
    author_in: AuthorSchema,
    author: Author = Depends(author_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await author_update(session=session, author=author, author_in=author_in)


@router.delete(
    "/{author_id}", summary="Удаление автора", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_author(
    author: Author = Depends(author_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await author_delete(session=session, author=author)
