from uuid import UUID

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse


router = APIRouter(prefix="/content")


@router.get("/{content_uid}", response_class=StreamingResponse)
async def get_content(content_uid: UUID) -> StreamingResponse:
    ...