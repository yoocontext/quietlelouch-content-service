from uuid import UUID

from fastapi import APIRouter, status
from fastapi.responses import FileResponse


router = APIRouter(prefix="/content")


@router.get(
    path="/{content_uid}",
    response_model=FileResponse,
    status_code=status.HTTP_200_OK,
)
async def get_content(content_uid: UUID) -> FileResponse:
    ...