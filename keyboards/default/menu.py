from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Регистрация")
        ],
        [
            KeyboardButton(text="Авторизация"),
            KeyboardButton(text="Изменить реквизиты")
        ]
    ],
    resize_keyboard=True
)