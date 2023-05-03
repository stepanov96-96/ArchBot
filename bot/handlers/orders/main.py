from bot.tools.keyboards import *
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.tools import utils
from bot.tools.keyboards import static_orders


async def orders(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, 'Прием заказов на:', inlines.orders())
    

async def turnoff(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, static_orders['turnoff']+':\n\nПозвонить по номеру тел. 200-277', inlines.back('orders:back'))
    

async def sealing(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, static_orders['sealing']+':\n\nОпломбировку счетчиков ХВС и ГВС производит Жилкомцентр по тел. 790-613', inlines.back('orders:back'))
    

async def back(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, 'Прием заяков на:', inlines.orders())
