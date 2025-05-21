from domain.values.base import BaseValue
from domain.values.exceptions import ImageTooLargeError


class ImageSizeValue(BaseValue[int, int]):
    max_size_mb = 13

    def validate(self):
        size_mb: float = round(self.value / 1024 / 1024, 2)

        if size_mb > self.max_size_mb:
            raise ImageTooLargeError(size=size_mb)

    def as_generic_type(self) -> int:
        return self.value