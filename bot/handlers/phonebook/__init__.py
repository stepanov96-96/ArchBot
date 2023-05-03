from aiogram import Dispatcher
from .main import *
from aiogram.dispatcher.filters import Text

index = str(list(static_options.keys()).index('phonebook'))
pb_keys = list(static_phonebook.keys())

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(phonebook, Text(equals='option:'+index))
    dp.register_callback_query_handler(office_telephone, Text(equals='phonebook:'+str(pb_keys.index('office_telephone'))))
    dp.register_callback_query_handler(emergency_telephone, Text(equals='phonebook:'+str(pb_keys.index('emergency_telephone'))))
    dp.register_callback_query_handler(clearing_center, Text(equals='phonebook:'+str(pb_keys.index('clearing_center'))))
    dp.register_callback_query_handler(filling, Text(equals='phonebook:'+str(pb_keys.index('filling'))))
    dp.register_callback_query_handler(set_replace_fill, Text(equals='phonebook:'+str(pb_keys.index('set_replace_fill'))))
    dp.register_callback_query_handler(gos_check, Text(equals='phonebook:'+str(pb_keys.index('gos_check'))))
    dp.register_callback_query_handler(back, Text(equals='phonebook:back'))