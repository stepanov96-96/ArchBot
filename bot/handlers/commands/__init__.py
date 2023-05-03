from aiogram import Dispatcher
from bot.tools.keyboards.config import static_buttons
from .main import *

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])