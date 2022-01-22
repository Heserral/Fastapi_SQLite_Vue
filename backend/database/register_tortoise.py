from typing import Optional

from tortoise import Tortoise


def register_tortoise(app, generate_schemas: bool = False) -> None:
    @app.on_event("startup")
    async def init_orm():
        await Tortoise.init(
          db_url='sqlite://db.sqlite3',
          modules={'models': ['database.models']}
        )
        if generate_schemas:
            await Tortoise.generate_schemas()

    @app.on_event("shutdown")
    async def close_orm():
        await Tortoise.close_connections()