from uuid import UUID
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

from application.api.v1.image.upload.mappers import CreateUploadCommandMapper
from application.api.v1.image.upload.schemas import CreateImageInSchema, CreateImageOutSchema, GetImageOutSchema
from di import get_container
from logic.use_cases.image.upload import (
    UploadImageUseCase,
    UploadImageCommand,
    UploadImageResult,
)
from logic.use_cases.image.get import (
    GetImageUseCase,
    GetImageCommand,
    GetImageResult,
)


router = APIRouter(prefix="/image")

ALLOWED_TYPES = {"image/jpeg", "image/png"}


@router.post(
    path="/upload",
    response_model=CreateImageOutSchema,
    status_code=status.HTTP_201_CREATED,
)
async def upload_image(
    in_schema: str = Form(..., alias="in_schema"),
    file: UploadFile = File(...),
    # user_uid: UUID = Depends(auth_by_token),
) -> CreateImageOutSchema:
    user_uid = UUID("d6d7e017-48c7-4fda-b776-34ac8130ed73")

    try:
        schema_data = CreateImageInSchema(**json.loads(in_schema))
    except (json.JSONDecodeError, ValueError) as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid schema JSON")
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported image type. Only JPEG and PNG are allowed."
        )

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

        return CreateImageOutSchema(
            url=result.url,
            width=result.width,
            height=result.height,
            size=result.size,
            content_type=result.content_type,
        )


@router.get(path="/{image_uid}", response_model=GetImageOutSchema)
async def get_image(
    image_uid: UUID,
    # user_uid: UUID = Depends(auth_by_token),
) -> GetImageOutSchema:
    container = get_container()
    async with container() as cont:
        use_case: GetImageUseCase = await cont.get(GetImageUseCase)
        command = GetImageCommand(image_uid=image_uid)

        result: GetImageResult = await use_case.act(command=command)

        return GetImageOutSchema(
            url=result.url,
            width=result.width,
            height=result.height,
            size=result.size,
            content_type=result.content_type,
        )
