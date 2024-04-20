from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Меню
main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Сделать заказ')],
                                     [KeyboardButton(text='Помощь')],
                                     [KeyboardButton(text='Контакты')]],
                                     resize_keyboard=True,
                                     input_field_placeholder='Пункт меню')

# Каталог
catalog =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Разработка сайта')],
                                               [InlineKeyboardButton(text='Разработка сайта')],
                                               [InlineKeyboardButton(text='Разработка сайта')]])