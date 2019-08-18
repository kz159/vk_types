from .base import BaseModel
from .attachments import Attachments, Geo
from enum import Enum

import typing


# https://vk.com/dev/objects/message


class Actions(Enum):
    chat_photo_update = "chat_photo_update"
    chat_photo_remove = "chat_photo_remove"
    chat_create = "chat_create"
    chat_title_update = "chat_title_update"
    chat_invite_user = "chat_invite_user"
    chat_kick_user = "chat_kick_user"
    chat_pin_message = "chat_pin_message"
    chat_unpin_message = "chat_unpin_message"
    chat_invite_user_by_link = "chat_invite_user_by_link"


class MessageActionPhoto(BaseModel):
    photo_50: str = None
    photo_100: str = None
    photo_200: str = None


class MessageAction(BaseModel):
    type: Actions = None
    member_id: int = None
    text: str = None
    email: str = None
    photo: MessageActionPhoto = None


class Message(BaseModel):
    id: int = None
    date: int = None
    peer_id: int = None
    from_id: int = None
    text: str = None
    random_id: int = None
    attachments: Attachments = None
    important: bool = None
    geo: Geo = None
    payload: str = None
    action: MessageAction = None
    fwd_messages: typing.List["Message"] = None

    async def reply(self, message: str, attachment: str = None):
        return await self.api.messages.send(
            message=message, peer_id=self.peer_id, attachment=attachment, reply_to=self.id,
        )

    async def answer(self, message: str, attachment: str = None):
        return await self.api.messages.send(
            message=message,
            peer_id=self.peer_id,
            attachment=attachment,
        )


Message.update_forward_refs()
