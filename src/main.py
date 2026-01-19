import asyncio
from aiogram import Bot, Dispatcher
from os import environ
from services import handler


async def telegram_bot() -> None:
    bot = Bot(environ["TELEGRAM_BOT_TOKEN"])

    dp = Dispatcher()
    dp.include_routers(handler.router)

    await dp.start_polling(bot)


asyncio.run(telegram_bot())