import asyncio
from aiogram import Bot, Dispatcher
import mysecrets
from services import handler


async def telegram_bot() -> None:
    bot = Bot(mysecrets.TELEGRAM_BOT_TOKEN)

    dp = Dispatcher()
    dp.include_routers(handler.router)

    await dp.start_polling(bot)


asyncio.run(telegram_bot())
