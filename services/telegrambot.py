import asyncio
from aiogram import Bot, Dispatcher
from app import handler
from os import environ


def start_telegram_bot() -> None:
    asyncio.run(telegram_bot())


async def telegram_bot() -> None:
    bot = Bot(environ.get("TELEGRAM_BOT_TOKEN"))

    dp = Dispatcher()
    dp.include_routers(handler.router)

    await dp.start_polling(bot)
