from application.api.v1.schemas import (
    TitleCreateSchema,
    AuthorCreateSchema,
    LanguageCreateSchema,
    RoleCreateSchema,
    TagCreateSchema,
)

from logic.use_cases.schemas import (
    TitleCreateCaseSchema,
    AuthorCreateCaseSchema,
    LanguageCreateCaseSchema,
    RoleCreateCaseSchema,
    TagCreateCaseSchema,
)


class CreateEntitySchemaMapper:
    @staticmethod
    def get_title(title: TitleCreateSchema) -> TitleCreateCaseSchema:
        title_case = TitleCreateCaseSchema(name=title.name)
        return title_case

    @staticmethod
    def get_author(author: AuthorCreateSchema) -> AuthorCreateCaseSchema:
        author_case = AuthorCreateCaseSchema(name=author.name, bio=author.bio)
        return author_case

    @staticmethod
    def get_language(language: LanguageCreateSchema) -> LanguageCreateCaseSchema:
        language_case = LanguageCreateCaseSchema(name=language.name, description=language.description)
        return language_case

    def get_roles(self, roles: list[RoleCreateSchema]) -> list[RoleCreateCaseSchema]:
        result: list[RoleCreateCaseSchema] = []
        for role in roles:
            role_case: RoleCreateCaseSchema = self._get_role(role=role)
            result.append(role_case)
        return result

    def get_tags(self, tags: list[TagCreateSchema]) -> list[TagCreateCaseSchema]:
        result: list[TagCreateCaseSchema] = []
        for tag in tags:
            tag_case: TagCreateCaseSchema = self._get_tag(tag=tag)
            result.append(tag_case)
        return result

    @staticmethod
    def _get_role(role: RoleCreateSchema) -> RoleCreateCaseSchema:
        role_case = RoleCreateCaseSchema(name=role.name, description=role.description)
        return role_case

    @staticmethod
    def _get_tag(tag: TagCreateSchema) -> TagCreateCaseSchema:
        tag_case = TagCreateCaseSchema(
            name=tag.name, description=tag.description,
        )
        return tag_case
