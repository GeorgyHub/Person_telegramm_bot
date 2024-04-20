from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Меню
main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Сделать заказ')],
                                     [KeyboardButton(text='Помощь')],
                                     [KeyboardButton(text='Контакты')]],
                                     resize_keyboard=True,
                                     input_field_placeholder='Пункт меню')

# Каталог
catalog =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Разработка сайта', callback_data='Web')],
                                               [InlineKeyboardButton(text='Разработка ботов', callback_data='bots')],
                                               [InlineKeyboardButton(text='Дизайн макетов', callback_data='disang')],
                                               [InlineKeyboardButton(text='Парсинг', callback_data='parsing')]])