import asyncio

from app.ws.server import start_server

if __name__ == "__main__":
    asyncio.run(start_server())
