from time import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from lib import db_selection
from keyboards.inline import menu, generate_celebs, generation_estimation, generating_more
from loader import dp
from states import UserMode


# завершить состояние + /menu
@dp.message_handler(Command('menu'), state=UserMode.celebs)  # /menu
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


@dp.message_handler(Command('menu'))  # /menu
async def user_register(message: types.Message):
    await message.answer(text=f'<b>--> Игра в шляпу🎩</b>\n'
                              f'Генерация селебрити/известных личностей\n'
                              f'Можно выбрать категории, либо просто рандомного человека/персонажа\n\n'
                              f'<b>--> Активити😈</b>\n'
                              f'Генерация слов для игры в активити\n'
                              f'Вместо слов на карточках генерируются слова (и не только🙈) в боте😍\n\n'
                              f'Выбери игру, в которую ты играешь снизу⬇️',
                         reply_markup=menu)


# выбор категорий + завершить состояние
@dp.callback_query_handler(text='Игра в шляпу', state=UserMode.celebs)
async def accept_id(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(f'Выбери категорию, по которой ты хочешь сгенерировать человека/персонажа\n\n'
                              f'либо же просто сгенерировать рандомно без выбора категории\n\n'
                              f'/menu - выход в главное меню',
                              reply_markup=generate_celebs)

    await state.finish()
    await UserMode.celebs.set()


# Кнопка: Игра в шляпу
@dp.callback_query_handler(text='Игра в шляпу')
async def accept_id(call: CallbackQuery):
    await call.message.edit_text(f'Выбери категорию, по которой ты хочешь сгенерировать человека/персонажа\n\n'
                                 f'либо же просто сгенерировать рандомно без выбора категории\n\n'
                                 f'/menu - выход в главное меню',
                                 reply_markup=generate_celebs)

    await UserMode.celebs.set()


@dp.callback_query_handler(text=['Киноиндустрия', 'Музыка', 'YouTube', 'Спорт', 'Политика', 'Бизнес',
                                 'Учёные/Писатели', 'Рандом'], state=UserMode.celebs)
async def accept_id(call: CallbackQuery, state: FSMContext):
    field_of_activity = call.data

    async with state.proxy() as data:
        data['field_of_activity'] = field_of_activity
        data['seq_number'] = 10

    await call.message.edit_text(f'Выбранная категория: <b>{field_of_activity}</b>\n\n'
                                 f'/menu - отмена всех действий и выход в главное меню\n\n'
                                 f'Генерация..')

    if field_of_activity == 'Рандом':
        text = await db_selection.full_random(seq_number=0)
    else:
        text = await db_selection.random_names(field_of_activity=field_of_activity, seq_number=0)

    sleep(0.5)
    await call.message.edit_text(f'Выбранная категория: <b>{field_of_activity}</b>\n\n'
                                 f'/menu - отмена всех действий и выход в главное меню\n\n'
                                 f'Генерация...')
    sleep(0.5)
    await call.message.edit_text(f'Выбранная категория: <b>{field_of_activity}</b>\n\n'
                                 f'/menu - отмена всех действий и выход в главное меню\n\n'
                                 f'Генерация....')
    sleep(0.5)

    await call.message.edit_text(f'Выбранная категория: <b>{field_of_activity}</b>\n\n'
                                 f'/menu - отмена всех действий и выход в главное меню')

    await call.message.answer(f'{text}')
    await call.message.answer(f'<i>*оцени снизу, как тебе генерация</i>',
                              reply_markup=generation_estimation)


@dp.callback_query_handler(text=['1⭐️', '2⭐️', '3⭐️', '4⭐️', '⭐️⭐️⭐️⭐️⭐️'],
                           state=UserMode.celebs)
async def accept_id(call: CallbackQuery, state: FSMContext):
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_text(f'Спасибо за оценку!\n\n'
                                 f'/menu - выход в главное меню\n\n'
                                 f'Нажми кнопку ниже, чтобы сгенерировать ещё или вернуться '
                                 f'к выбору категории',
                                 reply_markup=generating_more)


@dp.callback_query_handler(text='Сгенерировать ещё', state=UserMode.celebs)
async def accept_id(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    field_of_activity = data.get('field_of_activity')
    seq_number = data.get('seq_number')

    if field_of_activity == 'Рандом':
        text = await db_selection.full_random(seq_number)
    else:
        text = await db_selection.random_names(field_of_activity, seq_number)

    async with state.proxy() as data:
        data['seq_number'] += 10

    await call.message.edit_text(f'{text}')
    await call.message.answer(f'<i>*оцени снизу, как тебе генерация</i>',
                              reply_markup=generation_estimation)
