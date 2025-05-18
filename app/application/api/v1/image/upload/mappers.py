from dataclasses import dataclass
from uuid import UUID

from fastapi import UploadFile

from application.api.v1.mappers import CreateEntitySchemaMapper
from application.api.v1.image.upload.schemas import ImageCreateInSchema
from logic.use_cases.image import UploadImageCommand

from logic.use_cases.image.schemas import (
    TitleCreateCaseSchema,
    AuthorCreateCaseSchema,
    LanguageCreateCaseSchema,
    RoleCreateCaseSchema,
    TagCreateCaseSchema,
)


@dataclass
class CreateUploadCommandMapper:
    schemas_mapper: CreateEntitySchemaMapper

    def act(
        self,
        create_schema: ImageCreateInSchema,
        user_uid: UUID,
        file: UploadFile,
    ) -> UploadImageCommand:
        tags: list[TagCreateCaseSchema] = self.schemas_mapper.get_tags(tags=create_schema.tags)
        access_roles: list[RoleCreateCaseSchema] = self.schemas_mapper.get_roles(roles=create_schema.access_roles)
        language: LanguageCreateCaseSchema = self.schemas_mapper.get_language(language=create_schema.language)

        title: TitleCreateCaseSchema | None = None
        author: AuthorCreateCaseSchema | None = None

        if create_schema.title:
            title: TitleCreateCaseSchema = self.schemas_mapper.get_title(title=create_schema.title)

        if create_schema.author:
            author: AuthorCreateCaseSchema = self.schemas_mapper.get_author(author=create_schema.author)

        upload_command = UploadImageCommand(
            file=file,
            name=create_schema.name,
            description=create_schema.description,
            nsfw=create_schema.nsfw,
            user_uid=user_uid,
            tags=tags,
            access_roles=access_roles,
            title=title,
            author=author,
            language=language,
        )
        return upload_command
