from tortoise import fields
from tortoise.models import Model


class Chat(Model):
    id = fields.UUIDField(primary_key=True)
    users = fields.ManyToManyField("models.User", related_name="users")


class Messages(Model):
    id = fields.IntField(primary_key=True)
    chat = fields.ForeignKeyField("models.Chat", related_name="chat")
    sender = fields.ForeignKeyField("models.User", related_name="sender")
    receiver = fields.ForeignKeyField("models.User", related_name="receiver")
    message = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
