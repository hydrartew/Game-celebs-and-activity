from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminMode(StatesGroup):
    celebs = State()
    activity = State()


class UserMode(StatesGroup):
    celebs = State()
    activity = State()
