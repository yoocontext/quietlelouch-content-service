from uuid import UUID, uuid4
import json

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    UploadFile,
    File,
    Form,
    status,
)
from fastapi.responses import StreamingResponse

from application.api.v1.image.upload.mappers import CreateUploadCommandMapper
from application.api.v1.image.upload.schemas import ImageCreateInSchema, ImageCreateOutSchema
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
    schema: str = Form(...),
    file: UploadFile = File(...),
    # user_uid: UUID = Depends(...),
) -> ImageCreateOutSchema:
    user_uid = UUID("d6d7e017-48c7-4fda-b776-34ac8130ed73")

    try:
        schema_data = ImageCreateInSchema(**json.loads(schema))
    except (json.JSONDecodeError, ValueError) as e:
        raise HTTPException(status_code=400, detail="Invalid schema JSON") from e
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported image type. Only JPEG and PNG are allowed.")

    container = get_container()
    async with container() as cont:
        mapper: CreateUploadCommandMapper = await cont.get(CreateUploadCommandMapper)
        use_case: UploadImageUseCase = await cont.get(UploadImageUseCase)
        command: UploadImageCommand = mapper.act(
            create_schema=schema_data,
            file=file,
            user_uid=user_uid,
        )
        result: UploadImageResult = await use_case.act(command=command)

        return ImageCreateOutSchema(
            url=result.url,
            width=result.width,
            height=result.height,
            size=result.size,
            content_type=result.content_type,
        )



# @router.get(path="/{image_uid}/download", response_class=StreamingResponse)
# async def get_image(image_uid: UUID) -> StreamingResponse:
#     ...
