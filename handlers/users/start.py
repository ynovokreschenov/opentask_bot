from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link

from loader import dp
from re import compile


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"Здравствуйте, {message.from_user.full_name}!\n"
        f"Вас приветствует бот для работы с партнерами!"
        )


@dp.message_handler(CommandStart(deep_link="123"))
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Ты нажал на старт и передал аргумент 123!!!")


# регулярные выражения https://ihateregex.io
@dp.message_handler(CommandStart(deep_link=compile(r"^[0-9]{4,15}$")))
async def bot_start(message: types.Message):
    referral = message.get_args()
    await message.answer(f"Привет, {message.from_user.full_name}! Ты нажал на старт и передал правильный аргумент {referral}!!!")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    deep_link = await get_start_link(payload="1234")
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'В вашей команде нет диплинка.\n'
                         f'Ваша диплинк ссылка - {deep_link}')

