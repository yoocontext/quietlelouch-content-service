from dataclasses import dataclass

from domain.entities.author import Author
from domain.entities.content import Image
from domain.mappers.values import ContentValuesMapper
from domain.values.content.common import NameValue, TitleValue, DescriptionValue, MediaTypeValue
from domain.values.content.image import ImageSizeValue

from infra.pg.models import ImageOrm, AuthorOrm


@dataclass
class ImageOrmToEntityMapper:
    values_mapper: ContentValuesMapper

    def get_image(self, image_orm: ImageOrm) -> Image:
        name: NameValue = self.values_mapper.get_name_value(name=image_orm.name)
        media_type: MediaTypeValue = self.values_mapper.get_media_type(media_type=image_orm.media_type)
        size_value: ImageSizeValue = self.values_mapper.get_size(size=image_orm.size)

        title_value: TitleValue | None = None
        description_value: DescriptionValue | None = None

        if image_orm.title:
            title_value: TitleValue = self.values_mapper.get_title_value(title=image_orm.title.name)
        if image_orm.description:
            description_value: DescriptionValue = self.values_mapper.get_description(description=image_orm.description)

        image = Image(
            uid=image_orm.uid,
            name=name,
            title=title_value,
            description=description_value,
            media_type=media_type,
            size=size_value,
            width=image_orm.width,
            height=image_orm.height,
        )
        return image


@dataclass
class AuthorOrmToEntityMapper:
    values_mapper: ContentValuesMapper

    def get_author(self, author_orm: AuthorOrm) -> Author:
        ...


