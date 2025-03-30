import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = "7973080602:AAHvXptj0MbuMOpQSZ7mT2zidWZdTHYGJY4"  # O'z botingiz tokenini qo'ying

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Kino kodini yozing, men sizga topib beraman!")

executor.start_polling(dp, skip_updates=True)