from enum import Enum

from tortoise import fields
from tortoise.models import Model


class StatusEnum(Enum):
    active = "active"
    inactive = "inactive"


class Chat(Model):
    id = fields.UUIDField(primary_key=True)
    users = fields.ManyToManyField("models.User", related_name="users")
    status = fields.CharEnumField(enum_type=StatusEnum, default=StatusEnum.active)


class Message(Model):
    id = fields.IntField(primary_key=True)
    chat = fields.ForeignKeyField("models.Chat", related_name="chat")
    sender = fields.ForeignKeyField("models.User", related_name="sender")
    receiver = fields.ForeignKeyField("models.User", related_name="receiver")
    message = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)


class InitChatReq:
    def __init__(self, user_1, user_2) -> None:
        self.event = "init"
        self.user_1 = user_1
        self.user_2 = user_2
