import asyncio

from tortoise import Tortoise, run_async

from app.interface.app import Lahh
from app.utils.db import init
from app.ws.server import start_server

if __name__ == "__main__":
    app = Lahh()
    app.run()
