from dataclasses import dataclass

from domain.entities.content import Image
from domain.mappers.values import ContentValuesMapper
from domain.values.content import NameValue, TitleValue, DescriptionValue, MediaTypeValue

from infra.pg.models import ImageOrm


@dataclass
class ContentOrmToEntityMapper:
    values_mapper: ContentValuesMapper

    def get_image(self, image_orm: ImageOrm) -> Image:
        name: NameValue = self.values_mapper.get_name_value(name=image_orm.name)
        title: TitleValue | None = self.values_mapper.get_title_value(title=image_orm.title.name)
        description: DescriptionValue | None = self.values_mapper.get_description(description=image_orm.description)
        media_type: MediaTypeValue = self.values_mapper.get_media_type(media_type=image_orm.media_type)
        image = Image(
            uid=image_orm.uid,
            name=name,
            title=title,
            description=description,
            media_type=media_type,
        )
        return image
