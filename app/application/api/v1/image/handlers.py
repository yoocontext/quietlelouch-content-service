from uuid import UUID
import json

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    UploadFile,
    Response,
    File,
    Form,
    status,
)

from application.api.v1.image.mappers import (
    CreateUploadCommandMapper,
    CreateUpdateCommandMapper,
)
from application.api.v1.image.schemas import (
    UploadImageInSchema,
    CreateImageOutSchema,
    GetImageOutSchema,
    UpdateImageOutSchema,
    UpdateImageInSchema,
)
from di import get_container
from logic.use_cases.image.delete import (
    DeleteImageUseCase,
    DeleteImageCommand,
)
from logic.use_cases.image.update import (
    UpdateImageUseCase,
    UpdateImageCommand,
    UpdateImageResult,
)
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
        schema_data = UploadImageInSchema(**json.loads(in_schema))
    except (json.JSONDecodeError, ValueError):
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
            uid=result.uid,
            name=result.name,
            description=result.description,
            nsfw=result.nsfw,
            tags=result.tags,
            title=result.title,
            author=result.title,
            language=result.language,
            width=result.width,
            height=result.height,
            size=result.size,
            content_type=result.content_type,
            url=result.url,
        )


@router.get(
    path="/{image_uid}",
    response_model=GetImageOutSchema,
    status_code=status.HTTP_200_OK,
)
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
            uid=result.uid,
            name=result.name,
            description=result.description,
            nsfw=result.nsfw,
            tags=result.tags,
            title=result.title,
            author=result.title,
            language=result.language,
            width=result.width,
            height=result.height,
            size=result.size,
            content_type=result.content_type,
            url=result.url,
        )


@router.delete(
    path="/{image_uid}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_image(
    image_uid: UUID,
    # user_uid: UUID = Depends(auth_by_token),
) -> Response:
    container = get_container()
    async with container() as cont:
        use_case: DeleteImageUseCase = await cont.get(DeleteImageUseCase)
        command = DeleteImageCommand(image_uid=image_uid)
        await use_case.act(command=command)

        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch(
    path="/{image_uid}",
    response_model=UpdateImageOutSchema,
    status_code=status.HTTP_200_OK,
)
async def update_image(
    image_uid: UUID,
    in_schema: UpdateImageInSchema,
    # user_uid: UUID = Depends(auth_by_token),
) -> UpdateImageOutSchema:
    container = get_container()
    async with container() as cont:
        mapper: CreateUpdateCommandMapper = await cont.get(CreateUpdateCommandMapper)
        use_case: UpdateImageUseCase = await cont.get(UpdateImageUseCase)
        command: UpdateImageCommand = mapper.act(image_uid=image_uid, update_schema=in_schema)
        result: UpdateImageResult = await use_case.act(command=command)

        return UpdateImageOutSchema(
            uid=result.uid,
            name=result.name,
            description=result.description,
            nsfw=result.nsfw,
            tags=result.tags,
            title=result.title,
            author=result.title,
            language=result.language,
            width=result.width,
            height=result.height,
            size=result.size,
            content_type=result.content_type,
            url=result.url,
        )
