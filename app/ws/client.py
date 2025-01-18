import asyncio
import json

from websockets.asyncio.client import connect

from models.chat import InitChatReq, Message
from utils.env import uri


async def start_chat_request(user_1, user_2):
    async with connect(uri) as websocket:
        message = InitChatReq(user_1, user_2)
        await websocket.send(json.dumps(message))


async def send_message_to_server(
    websocket,
    chat: str,
    sender: str,
    receiver: str,
    message: str,
):
    content = Message(chat=chat, sender=sender, receiver=receiver, message=message)
    await websocket.send(json.dumps(content))


async def receive_message_from_server(websocket):
    response = await websocket.recv()
    data = json.loads(response)
    return data


async def handler():
    return
