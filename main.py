import logging
from aiogram import Bot, Dispatcher, executor
import asyncio
import aioschedule
import os

API_TOKEN: str = os.getenv('BOT_TOKEN')  # не забудь добавить переменную среды в .env
CHAT_ID: str = os.getenv('CHAT')  # не забудь добавить переменную среды в .env

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.DEBUG)


async def noon_print():
    await bot.send_message(chat_id=CHAT_ID, text='Go to DAILY, motherfucker')


async def scheduler():
    aioschedule.every(40).minutes.do(noon_print)
    # aioschedule.every().hour.do(job)
    aioschedule.every().day.at("08:45").do(noon_print)
    # aioschedule.every().monday.do(job)
    aioschedule.every().friday.at("08:50").do(noon_print)
    # aioschedule.every().minute.at(":17").do(job)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
