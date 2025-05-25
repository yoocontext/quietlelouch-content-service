from infra.pg.models import (
    TagOrm,
    RoleOrm,
    TitleOrm,
    AuthorOrm,
    LanguageOrm,
)

from infra.pg.dto.create import (
    TagCreateSchema,
    RoleCreateSchema,
    TitleCreateSchema,
    AuthorCreateSchema,
    LanguageCreateSchema,
)


class ContentCreateSchemaToOrmMapper:
    @staticmethod
    def create_tags(tags: list[TagCreateSchema]) -> list[TagOrm]:
        tags_orm: list[TagOrm] = []
        for tag in tags:
            tag_orm = TagOrm(name=tag.name, description=tag.description)
            tags_orm.append(tag_orm)
        return tags_orm

    @staticmethod
    def create_access_roles(access_roles: list[RoleCreateSchema]) -> list[RoleOrm]:
        roles_orm: list[RoleOrm] = []
        for role in access_roles:
            role_orm = RoleOrm(name=role.name, description=role.description)
            roles_orm.append(role_orm)
        return roles_orm

    @staticmethod
    def create_title(title: TitleCreateSchema) -> TitleOrm:
        title_orm = TitleOrm(name=title.name)
        return title_orm

    @staticmethod
    def create_author(author: AuthorCreateSchema) -> AuthorOrm:
        author_orm = AuthorOrm(name=author.name, bio=author.bio)
        return author_orm

    @staticmethod
    def create_language(language: LanguageCreateSchema) -> LanguageOrm:
        language_orm = LanguageOrm(name=language.name, description=language.description)
        return language_orm