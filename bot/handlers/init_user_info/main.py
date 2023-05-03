from bot.tools.keyboards import *
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.tools import fsm
from bot.tools.keyboards import inlines
from bot.tools import database


async def set_name(msg: types.Message, state:FSMContext):
    fio = msg.text
    await state.update_data(fio=fio)
    await msg.answer('Введите номер квартиры')
    await state.set_state(fsm.UserInfo.flat)
    

async def set_flat(msg: types.Message, state:FSMContext):
    flat = msg.text
    await state.update_data(flat=flat)
    await msg.answer('Введите номер лицевого счета')
    await state.set_state(fsm.UserInfo.account_number)
    
    
async def set_account_number(msg: types.Message, state:FSMContext):
    account_number = msg.text
    telegram_id = msg.from_user.id
    
    async with state.proxy() as data:
        fio = data['fio']
        flat = data['flat']
        
        database.add_user(telegram_id, fio, flat, account_number)
        
        await state.finish()
    
    
    await msg.answer('Приветствуем вас в меню бота, наш бот умеет:', reply_markup=inlines.options())
    
    