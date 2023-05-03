from aiogram import Dispatcher
from .main import *
from aiogram.dispatcher.filters import Text
from bot.tools.keyboards import static_options


index = str(list(static_options.keys()).index('schedule'))

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(schedule, Text(equals='option:'+index))