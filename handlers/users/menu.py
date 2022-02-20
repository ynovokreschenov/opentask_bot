from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove, Message

from keyboards.default import menu
from loader import dp
from utils.misc import dadata


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выберите действие", reply_markup=menu)


@dp.message_handler(Text(equals=["Проверка ИНН"]))
async def get_register(message: Message):
    #await message.answer(f"Вы выбрали {message.text}", reply_markup=ReplyKeyboardRemove())
    await message.answer(f"Вы выбрали {message.text}", reply_markup=ReplyKeyboardRemove())

