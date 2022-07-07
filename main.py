#!venv/bin/python

import logging
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import aioschedule
from os import environ

API_TOKEN: str = environ.get('BOT_TOKEN') # не забудь добавить переменную среды в .env

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


async def noon_print():
    await bot.send_message(-1001608864323, 'Go to DAYLY, motherfucker')


async def scheduler():
    aioschedule.every().day.at("21:08").do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
