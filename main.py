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


async def go_daily():
    await bot.send_message(chat_id=CHAT_ID, text='Пора на дейли')


async def task_close():
    await bot.send_message(chat_id=CHAT_ID, text='А ты закрыл Задачу?')


async def task_close_image():
    photo = open("files/task_image.jpg", 'rb')
    await bot.send_photo(chat_id=CHAT_ID, photo=photo)
    photo.close()


async def scheduler():
    # aioschedule.every(5).minutes.do(noon_print)
    # aioschedule.every(3).minutes.do(task_close_image)
    # aioschedule.every().hour.do(job)
    #aioschedule.every().day.at("12:15").do(noon_print)
    # aioschedule.every().monday.do(job)
    aioschedule.every().monday.at("06:55").do(go_daily)
    aioschedule.every().monday.at("15:00").do(task_close_image)
    aioschedule.every().tuesday.at("06:55").do(go_daily)
    aioschedule.every().tuesday.at("15:00").do(task_close_image)
    aioschedule.every().wednesday.at("06:55").do(go_daily)
    aioschedule.every().wednesday.at("15:00").do(task_close_image)
    aioschedule.every().thursday.at("06:55").do(go_daily)
    aioschedule.every().thursday.at("15:00").do(task_close_image)
    aioschedule.every().friday.at("06:55").do(go_daily)
    aioschedule.every().friday.at("15:00").do(task_close_image)
    # aioschedule.every().minute.at(":17").do(job)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
