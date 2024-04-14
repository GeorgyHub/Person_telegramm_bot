import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
# Bot API_TOKEN
API_TOKEN = '6571262110:AAHnhi_QsZCY_vSef0qcktpIlMQ88Q-qzk8'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Menu

# Commands
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply('Hello world!')

@dp.message_handler()
async def echo(message: types.Message):
   await message.answer(message.text)

# Start process
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())