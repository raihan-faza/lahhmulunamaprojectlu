from tortoise import Tortoise, run_async


async def init():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3", modules={"models": ["app.models"]}
    )
    await Tortoise.generate_schemas()
