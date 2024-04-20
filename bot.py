import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from app.handlers import router

# Bot API_TOKEN
async def main():
    bot = Bot(token='6571262110:AAHnhi_QsZCY_vSef0qcktpIlMQ88Q-qzk8')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

# Menu

# Commands

if __name__ == "__main__":
   try:
       asyncio.run(main())
   except KeyboardInterrupt:
       print('Бот отключён')