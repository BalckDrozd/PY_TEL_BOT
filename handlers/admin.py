from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from data_base import sqlite_db


class FSMAdmin(StatesGroup):
    name = State()


# Поиск по названию
@dp.message_handler(commands='Найти_Фильм', state=None)
async def find_name(message: types.Message):
    await FSMAdmin.name.set()
    await message.reply('Введите название фильма')


# Ловим ответ
@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    name_film = message.text
    await sqlite_db.find_Film_name(message)
    await state.finish()


def register_handlers_admin(dp: Dispatcher):
    # dp.register_message_handler(find_random, commands=['Случайный_Фильм'])
    # dp.register_message_handler(find_name, commands='Найти_Фильм', state=None)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
