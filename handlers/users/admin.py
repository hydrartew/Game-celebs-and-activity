import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from lib import db_changes, db_selection
from keyboards.inline import menu_admin, generate_celebs
from lib import db_changes
from loader import dp
from states import AdminMode
from utils.misc import rate_limit
from lib.config import admins


@dp.message_handler(Command('cancel'), state=[AdminMode.celebs, AdminMode.activity])  # /cancel
async def user_register(message: types.Message, state: FSMContext):
    await message.answer(text=f'Отменено.')

    await state.finish()


@dp.message_handler(Command('admin'), user_id=admins)  # /admin
async def user_register(message: types.Message):
    await message.answer(text=f'Выбери игру, в в какую игру ты хочешь добавить слова/имена\n\n'
                              f'/cancel - отмена всех действий',
                         reply_markup=menu_admin)


# Кнопка: Игра в шляпу
@dp.callback_query_handler(text='Admin hat')
async def accept_id(call: CallbackQuery):
    await call.message.edit_text(f'Выбери категорию, ты хочешь добавить имена\n\n'
                                 f'/cancel - отмена всех действий',
                                 reply_markup=generate_celebs)

    await AdminMode.celebs.set()


@dp.callback_query_handler(text=['Киноиндустрия', 'Музыка', 'YouTube', 'Спорт', 'Политика', 'Бизнес',
                                 'Учёные/Писатели'], state=AdminMode.celebs)
async def accept_id(call: CallbackQuery, state: FSMContext):
    field_of_activity = call.data

    async with state.proxy() as data:
        data['field_of_activity'] = field_of_activity

    await call.message.edit_text(f'Выбранная категория: <b>{field_of_activity}</b>\n\n'
                                 f'Отправь список знаменитостей ниже\n\n'
                                 f'/cancel - отмена всех действий')


@dp.message_handler(state=AdminMode.celebs)
async def user_register(message: types.Message, state: FSMContext):
    celebs = message.text.split('\n')

    data = await state.get_data()
    field_of_activity = data.get('field_of_activity')

    for name in celebs:
        await db_changes.add_celeb(name, field_of_activity)

    async with state.proxy() as data:
        data['field_of_activity'] = field_of_activity

    await message.answer(f'Добавлено в категорию <b>{field_of_activity}</b>\n\n'
                         f'Если нужно добавить ещё, пришли сообщением снизу\n\n'
                         f'/cancel - отмена всех действий')


# Кнопка: Активити
@dp.callback_query_handler(text='Admin activity')
async def accept_id(call: CallbackQuery):
    await call.message.edit_text(f'Пришли ниже список слов/словосочетаний\n\n'
                                 f'/cancel - отмена всех действий')

    await AdminMode.activity.set()


@dp.message_handler(state=AdminMode.activity)
async def accept_id(message: types.Message):
    text_for_game = message.text.split('\n')

    for text in text_for_game:
        await db_changes.add_text(text)

    await message.answer(f'Слова/словосочетания добавлены\n\n'
                         f'Если нужно добавить ещё, пришли сообщением снизу\n\n'
                         f'/cancel - отмена всех действий')
