from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Найти_Фильм')
#b2 = KeyboardButton('/Поиск_по_описанию')
b3 = KeyboardButton('/Случайный_Фильм')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b3)
