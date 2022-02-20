from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.user import User

from utils.misc.dadata import check_status

# Сделаем фильтр на команду /test, где не будет указано никакого состояния
@dp.message_handler(Command("inn"), state=None)
async def enter_inn(message: types.Message):
    await message.answer("Введите ИНН:")

    # Вариант 1 - с помощью функции сет
    await User.inn.set()

    # Вариант 2 - с помощью first
    # await Test.first()


@dp.message_handler(state=User.inn)
async def answer_inn(message: types.Message, state: FSMContext):
    answer = message.text

    # Вариант 2 получения state
    # state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    # Вариант 1 сохранения переменных - записываем через key=var
    # Если у вас запись идет какого-то параметра (например email) то записывайте не answer,
    # а email, чтобы потом было понятно что именно доставать
    await state.update_data(inn=answer)

    # Вариант 2 - передаем как словарь
    await state.update_data(
        {"inn": answer}
    )

    # Вариант 3 - через state.proxy
    async with state.proxy() as data:
        data["inn"] = answer
        # Удобно, если нужно сделать data["some_digit"] += 1
        # Или data["some_list"].append(1), т.к. не нужно сначала доставать из стейта, А потом задавать

    #await message.answer("Вопрос №2. \n\n"
    #                     "Ваша память ухудшилась и вы помните то, что было давно, но забываете недавние события?")

    #await Test.next()
    inn = data.get("inn")
    status = check_status(inn)
    await message.answer(f"Ваш статус Смозанятый: {status}")
    


#===@dp.message_handler(state=User.Q2)
#===async def answer_q2(message: types.Message, state: FSMContext):
    # Достаем переменные
    #===data = await state.get_data()
    #===answer1 = data.get("answer1")
    #===answer2 = message.text

    #===await message.answer("Спасибо за ваши ответы!")

    #print(answer1)
    #print(answer2)
    # Вариант 1
    #====await state.finish()

    # Вариант завершения 2
    # await state.reset_state()

    # Вариант завершения 3 - без стирания данных в data
    # await state.reset_state(with_data=False)