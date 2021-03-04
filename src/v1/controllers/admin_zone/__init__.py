from fastapi import APIRouter

from .tables import router as table_router


router = APIRouter(
    prefix="/admin"
)
router.include_router(table_router)
