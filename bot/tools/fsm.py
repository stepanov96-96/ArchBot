from aiogram.dispatcher.filters.state import State, StatesGroup

class UserInfo(StatesGroup):
    fio = State()
    flat = State()
    account_number = State()