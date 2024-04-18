from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

# При запуске
start = ReplyKeyboardMarkup(Keyboard = [[KeyboardButton(text='Старт')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите кнопку')

# Меню
main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Сделать заказ')],
                                     [KeyboardButton(text='Помощь')],
                                     [KeyboardButton(text='Контакты')]],
                                     resize_keyboard=True,
                                     input_field_placeholder='Check a button')

# Каталог
catalog =InlineKeyboardMarkup()