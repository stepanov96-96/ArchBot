from aiogram import Dispatcher
from .main import *


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(set_name, state=fsm.UserInfo.fio)
    dp.register_message_handler(set_flat, state=fsm.UserInfo.flat)
    dp.register_message_handler(set_account_number, state=fsm.UserInfo.account_number)