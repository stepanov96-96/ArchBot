from bot.tools.keyboards import *
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.tools import database, utils, fsm

async def start(msg: types.Message, state:FSMContext):
    await msg.answer('Для начала давайте с вами познакомимся, укажити свое ФИО')
    await state.set_state(fsm.UserInfo.fio)