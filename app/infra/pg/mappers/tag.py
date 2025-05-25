from dataclasses import dataclass

from domain.entities.content import Tag
from domain.mappers.values import ContentValuesMapper
from domain.values.content.common import NameValue, DescriptionValue
from infra.pg.models import TagOrm


@dataclass
class TagEntityMapper:
    values_mapper: ContentValuesMapper

    def tags_from_orm(self, tags_orm: list[TagOrm]) -> list[Tag]:
        tags: list[Tag] = []
        for tag_orm in tags_orm:
            tag: Tag = self._tag_from_orm(tag_orm=tag_orm)
            tags.append(tag)
        return tags

    def _tag_from_orm(self, tag_orm: TagOrm) -> Tag:
        name: NameValue = self.values_mapper.get_name_value(name=tag_orm.name)
        description: DescriptionValue = self.values_mapper.get_description(description=tag_orm.description)
        tag = Tag(uid=tag_orm.uid, name=name, description=description)
        return tag
