from uuid import UUID

from fastapi import UploadFile

from application.api.v1.image.schemas import (
    UploadImageInSchema,
    UpdateImageInSchema,
    UpdateTags,
    UpdateAccessRoles
)
from logic.use_cases.image import UploadImageCommand
from logic.use_cases.image.update import UpdateImageCommand


class CreateUploadCommandMapper:
    @staticmethod
    def act(
        create_schema: UploadImageInSchema,
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


class CreateUpdateCommandMapper:
    def act(
        self,
        image_uid: UUID,
        update_schema: UpdateImageInSchema
    ) -> UpdateImageCommand:
        tags = self._get_tags(in_tag=update_schema.tags)
        access_roles = self._get_roles(in_roles=update_schema.access_roles)
        command = UpdateImageCommand(
            image_uid=image_uid,
            tags=tags,
            access_roles=access_roles,
            name=update_schema.name,
            description=update_schema.description,
            nsfw=update_schema.nsfw,
            title=update_schema.title,
            author=update_schema.author,
            language=update_schema.language,
            fields_set=update_schema.model_fields_set,
        )
        return command

    @staticmethod
    def _get_tags(in_tag: UpdateTags) -> UpdateImageCommand.UpdateTags | None:
        if in_tag:
            tags = UpdateImageCommand.UpdateTags(
                to_add=in_tag.to_add,
                to_remove=in_tag.to_remove,
            )
            return tags

    @staticmethod
    def _get_roles(in_roles: UpdateAccessRoles) -> UpdateImageCommand.UpdateAccessRoles | None:
        if in_roles:
            roles = UpdateImageCommand.UpdateAccessRoles(
                to_add=in_roles.to_add,
                to_remove=in_roles.to_remove,
            )
            return roles