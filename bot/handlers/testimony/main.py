from bot.tools.keyboards import *
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.tools import utils


async def testimony(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, 'Какие показания вы хотите передать?', inlines.testimony())
    