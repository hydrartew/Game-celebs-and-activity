from time import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from lib import db_selection
from keyboards.inline import menu, generate_celebs, generation_estimation, generating_more, generating_words
from loader import dp
from states import UserMode
from utils.misc import rate_limit


# завершить состояние + /menu
@dp.message_handler(Command('menu'), state=UserMode.activity)  # /menu
async def user_register(message: types.Message, state: FSMContext):
    await message.answer(text=f'<b>--> Игра в шляпу🎩</b>\n'
                              f'Генерация селебрити/известных личностей\n'
                              f'Можно выбрать категории, либо просто рандомного человека/персонажа\n\n'
                              f'<b>--> Активити😈</b>\n'
                              f'Генерация слов для игры в активити\n'
                              f'Вместо слов на карточках генерируются слова (и не только🙈) в боте😍\n\n'
                              f'Выбери игру, в которую ты играешь снизу⬇️',
                         reply_markup=menu)

    await state.finish()


# Кнопка: "Активити"
@dp.callback_query_handler(text='Активити')
async def accept_id(call: CallbackQuery):
    await call.message.edit_text(f'Нажми кнопку ниже, если готов к игре. На выбор будет дано 3 слова/словосочетания\n\n'
                                 f'<i>P.s. после генерации <b>КД 1мин.</b> дабы избежать читерства🤗</i>',
                                 reply_markup=generating_words)

    await UserMode.activity.set()


@dp.callback_query_handler(text='Сгенерировать', state=UserMode.activity)
async def accept_id(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=None)
    words = await db_selection.select_random_words()
    await call.message.answer(f'{words}')
    sleep(60)
    await call.message.answer(f'КД прошло🫥 можешь сгенирировать ещё...\n\n'
                              f'/menu - выход в главное меню',
                              reply_markup=generating_words)
