from fastapi import FastAPI
from api.core import UserHandler
from provider.DatabaseProvider import engine
from model.User import User


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.drop_all)
        await conn.run_sync(User.metadata.create_all)


app = FastAPI()
app.include_router(UserHandler.router)
