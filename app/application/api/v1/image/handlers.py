from uuid import UUID

from fastapi import (
    APIRouter,
    HTTPException,
    UploadFile,
    File,
    status
)
from fastapi.responses import StreamingResponse

from application.api.v1.image.schemas import ImageCreateInSchema, ImageCreateOutSchema
from di import get_container
from logic.use_cases.image.upload import (
    UploadImageUseCase,
    UploadImageCommand,
    UploadImageResult,
)


router = APIRouter(prefix="/image")

ALLOWED_TYPES = {"image/jpeg", "image/png"}


@router.post(
    path="/upload",
    response_model=ImageCreateOutSchema,
    status_code=status.HTTP_201_CREATED,
)
async def upload_image(
    schema: ImageCreateInSchema,
    file: UploadFile = File(...)
) -> ImageCreateOutSchema:
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported image type. Only JPEG and PNG are allowed.")

    container = get_container()
    async with container() as cont:
        use_case: UploadImageUseCase = await cont.get(UploadImageUseCase)
        command = UploadImageCommand(
            file=file.file,
        )
        result: UploadImageResult = await use_case.act(command=command)
        ...



@router.get(path="/{image_uid}/download", response_class=StreamingResponse)
async def get_image(image_uid: UUID) -> StreamingResponse:
    ...
