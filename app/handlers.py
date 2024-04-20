from aiogram import F, Router
from aiogram.types import Message, callback_query
from aiogram.filters import CommandStart, Command

import app.keyboard as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)

@router.message(F.text == 'Помощь')
async def cmd_help(message: Message):
    await message.answer('Чем могу вам подсказать?')

@router.message(F.text == 'Контакты')
async def cmd_contact(message: Message):
    await message.answer('Мои контакты для связи')
    await message.answer('''Вконтакте: https://vk.com/goshanpol
                        Instagramm: https://www.instagram.com/georgy.polkanov/
                        Telegramm: https://t.me/GoshanPol''')

@router.message(F.text == 'Сделать заказ')
async def frontend(message: Message):
    await message.answer('Выберите категорию заказа', reply_markup=kb.catalog)

@router.callback_query(F.data == 'Web')
async def Web(callback: callback_query):
    await callback.answer('Опишите ТЗ', show_alert=True)
    await callback.message.answer('Опишите ТЗ')