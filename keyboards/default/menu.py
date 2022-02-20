from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            #KeyboardButton(text="Проверка ИНН")
        ],
        #[
        #    KeyboardButton(text="Авторизация"),
        #    KeyboardButton(text="Изменить реквизиты")
        #]
    ],
    resize_keyboard=True
)