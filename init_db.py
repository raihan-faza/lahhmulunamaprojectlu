from tortoise import run_async

from app.utils.db import init

if __name__ == "__main__":
    run_async(init())
