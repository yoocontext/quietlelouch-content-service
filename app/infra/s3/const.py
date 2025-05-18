from enum import Enum

class Bucket(Enum):
    MANGA = "manga"
    IMAGE = "image"
    GIF = "gif"
    VIDEO = "video"


class ClientMethod(Enum):
    GET_OBJECT = "get_object"
