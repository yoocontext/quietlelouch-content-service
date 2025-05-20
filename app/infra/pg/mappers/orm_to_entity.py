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
        media_type: MediaTypeValue = self.values_mapper.get_media_type(media_type=image_orm.media_type)

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
        )
        return image
