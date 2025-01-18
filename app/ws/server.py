import asyncio
import json

from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosedOK

from models.chat import Chat
from utils.env import port

active_chats = {}


async def start_chat(websocket, user_1, user_2):
    chat = Chat()
    await chat.users.add(user_1, user_2)
    active_chats[chat.id] = websocket


async def end_chat(websocket, chat_id):
    websocket.close()
    active_chats.pop(chat_id, None)


# handle client request
async def handler(websocket):
    while True:
        try:
            message = await asyncio.wait(websocket.recv(), timeout=1800)

        except asyncio.TimeoutError:
            break


async def start_server():
    async with serve(handler, "", int(port)):
        await asyncio.get_running_loop().create_future()
