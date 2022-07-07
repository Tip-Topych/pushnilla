#!venv/bin/python

import logging
from aiogram import Bot, Dispatcher, executor
import asyncio
import aioschedule
import config
from os import environ

API_TOKEN: str = environ.get('BOT_TOKEN')  # не забудь добавить переменную среды в .env

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

if not config.BOT_TOKEN:
    exit("No token provided")


async def noon_print():
    await bot.send_message(-1001608864323, 'Go to DAILY, motherfucker')


async def scheduler():
    aioschedule.every(1).minutes.do(noon_print)
    # aioschedule.every().hour.do(job)
    aioschedule.every().day.at("21:40").do(noon_print)
    # aioschedule.every().monday.do(job)
    # aioschedule.every().wednesday.at("13:15").do(job)
    # aioschedule.every().minute.at(":17").do(job)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
