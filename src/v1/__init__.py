from fastapi import APIRouter

from .controllers.admin_zone import router as admin_router
from .controllers.client_zone import router as client_router


router = APIRouter(
    prefix="/v1"
)
router.include_router(admin_router)
router.include_router(client_router)
