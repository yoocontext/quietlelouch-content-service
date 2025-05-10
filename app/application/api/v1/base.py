from fastapi import APIRouter
from handlers import router as content_router


router = APIRouter(prefix="/v1")
router.include_router(content_router)