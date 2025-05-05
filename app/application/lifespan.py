from contextlib import asynccontextmanager

from dishka import AsyncContainer
from fastapi import FastAPI
from faststream.rabbit import RabbitBroker

from application.events.handlers import router
from di import get_container


@asynccontextmanager
async def lifespan(app: FastAPI):
    container: AsyncContainer = await get_container()
    async with container() as cont:
        broker: RabbitBroker = await cont.get(RabbitBroker)
        broker.include_router(router)
        yield
