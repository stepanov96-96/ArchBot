from aiogram import Dispatcher
from .main import *
from aiogram.dispatcher.filters import Text

index = str(list(static_options.keys()).index('debt'))

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(debt, Text(equals='option:'+index))