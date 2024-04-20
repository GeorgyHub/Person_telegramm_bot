from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
#import app.keyboard as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Чем могу вам подсказать?')

@router.message(Command('Contact'))
async def cmd_contact(message: Message):
    await message.answer('Мои контакты для связи')
    await message.answer('''Вконтакте: https://vk.com/goshanpol
                        Instagramm: https://www.instagram.com/georgy.polkanov/
                        Telegramm: https://t.me/GoshanPol''')

@router.message(F.text == 'Сделать заказ')
async def frontend(message: Message):
    await message.answer('Выберите категорию заказа')