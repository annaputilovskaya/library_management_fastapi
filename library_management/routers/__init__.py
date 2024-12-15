from fastapi import APIRouter

from routers.author_router import router as author_router
from routers.book_router import router as book_router

router = APIRouter()
router.include_router(author_router)
router.include_router(book_router)
