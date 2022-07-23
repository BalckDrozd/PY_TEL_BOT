from aiogram import types, Dispatcher
from create_bot import dp, bot
from keybords import kb_client
from data_base import sqlite_db


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать, что будем смотреть?', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply(message.text)


#@dp.message_handler(commands=['Найти_Фильм'])
async def find_name(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите название')


#@dp.message_handler(commands=['Поиск по описанию'])
# async def find_opisanie(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Введите пару слов про фильм')

#@dp.message_handler(commands=['Случайный'])
async def find_random(message: types.Message):
    await bot.send_message(message.from_user.id, 'Незнаете что посмотреть?')
    #await bot.send_message(1034862828, 'Пашуля посмотрела')
    await sqlite_db.find_Film_random(message)

def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(find_name, commands=['Найти_Фильм'])
    #dp.register_message_handler(find_opisanie, commands=['Поиск_по_описанию'])
    dp.register_message_handler(find_random, commands=['Случайный_Фильм'])


