from bot.tools.keyboards import *
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.tools import utils


async def paylist(callback: types.CallbackQuery, state:FSMContext):
    file = open('bot/media/paylist.txt', 'rb')
    await utils.send_document(callback, state, document=file, caption='Ваша квитанция оплаты:')
    
    