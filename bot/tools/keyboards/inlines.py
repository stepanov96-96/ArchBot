from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .config import *


def options():
    markup = InlineKeyboardMarkup(row_width=1)
    
    for index, value in enumerate(static_options.values()):
        if value == static_options['dispatcher']:
            markup.add(InlineKeyboardButton(value, url='https://uk7.su'))
        else:    
            markup.add(InlineKeyboardButton(value, callback_data='option:'+str(index)))
    
    return markup


def phonebook():
    markup = InlineKeyboardMarkup(row_width=1)
    
    for index, value in enumerate(static_phonebook.values()):
        markup.add(InlineKeyboardButton(value, callback_data='phonebook:'+str(index)))
    
    return markup

# Phonebook
def pb_telephone(number:str|int):
    markup = InlineKeyboardMarkup(row_width=1)
    
    markup.add(InlineKeyboardButton(number, callback_data='empty'))
    markup.add(InlineKeyboardButton(static_buttons['back'], callback_data='phonebook:back'))

    return markup


def shedule():
    markup = InlineKeyboardMarkup(row_width=1)
    
    for el in static_shedule:
        markup.add(InlineKeyboardButton(el, callback_data='empty'))

    return markup
        


def testimony():
    markup = InlineKeyboardMarkup(row_width=1)
    
    markup.add(InlineKeyboardButton('Холодной, горячей воды и отопление', url='https://zkc-nk.ru/#input_ppu'))
    markup.add(InlineKeyboardButton('Электроэнергии', url='https://кузбассэнергосбыт.рф/'))
    
    return markup


def orders():
    markup = InlineKeyboardMarkup(row_width=1)
    
    for index, value in enumerate(static_orders.values()):
        markup.add(InlineKeyboardButton(value, callback_data='orders:'+str(index)))
    
    return markup


def back(callback_data:str='back'):
    markup = InlineKeyboardMarkup(row_width=1)
    
    markup.add(InlineKeyboardButton(static_buttons['back'], callback_data=callback_data))
    
    return markup