from uuid import UUID

from fastapi import UploadFile

from application.api.v1.image.upload.schemas import CreateImageInSchema
from logic.use_cases.image import UploadImageCommand


class CreateUploadCommandMapper:
    def act(
        self,
        create_schema: CreateImageInSchema,
        user_uid: UUID,
        file: UploadFile,
    ) -> UploadImageCommand:
        upload_command = UploadImageCommand(
            file=file,
            name=create_schema.name,
            description=create_schema.description,
            nsfw=create_schema.nsfw,
            user_uid=user_uid,
            tags=create_schema.tags,
            access_roles=create_schema.access_roles,
            title=create_schema.title,
            author=create_schema.author,
            language=create_schema.language,
        )
        return upload_command
