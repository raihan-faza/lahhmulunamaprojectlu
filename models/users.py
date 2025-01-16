from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(primary_key=True)
    username = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)
    chat_rooms = fields.ManyToManyField("models.Chat", related_name="chat_rooms")
    friends = fields.ManyToManyField("models.User", related_name="friends")
