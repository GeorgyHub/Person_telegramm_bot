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
    await message.reply('Вконтакте: https://vk.com/goshanpol')