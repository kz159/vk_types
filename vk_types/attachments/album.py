from ..base import BaseModel

from vk_types.attachments import Photo


class Album(BaseModel):
    id: int = None
    thumb: Photo = None
    owner_id: int = None
    title: str = None
    description: str = None
    created: int = None
    updated: int = None
    size: int
