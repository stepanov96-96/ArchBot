from aiogram import Dispatcher
from .main import *
from aiogram.dispatcher.filters import Text
from bot.tools.keyboards import static_orders

index = str(list(static_options.keys()).index('orders'))
orders_keys = list(static_orders.keys())

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(orders, Text(equals='option:'+index))
    dp.register_callback_query_handler(turnoff, Text(equals='orders:'+str(orders_keys.index('turnoff'))))
    dp.register_callback_query_handler(sealing, Text(equals='orders:'+str(orders_keys.index('sealing'))))
    dp.register_callback_query_handler(back, Text(equals='orders:back'))