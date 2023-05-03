from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from .config import *


def remove_keyboard():
    return ReplyKeyboardRemove()


def have_key():
    yes = KeyboardButton(static_buttons['yes'])
    no = KeyboardButton(static_buttons['no'])
    return ReplyKeyboardMarkup(resize_keyboard=True).add(yes, no)


def prensent():
    button = KeyboardButton(static_buttons['present'])
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button)

def cansel():
    button = KeyboardButton(static_buttons['cansel'])
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button)