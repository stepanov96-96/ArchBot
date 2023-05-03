from bot.tools.keyboards import *
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.tools import utils


async def phonebook(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, 'Телефонная книга:', markup=inlines.phonebook())
    
    
async def office_telephone(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, 'Телефон офиса:', markup=inlines.pb_telephone('200-27'))
    

async def emergency_telephone(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, 'Телефон аварийной службы (круглосуточно):', inlines.pb_telephone('200-277'))
    

async def clearing_center(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, 'Расчетный центр и паспортный стол:', inlines.pb_telephone('60-13-13'))


async def filling(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, 'Пломбировка счетчиков ГВ и ХВ:', inlines.pb_telephone('790-613'))
    

async def set_replace_fill(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, 'Установка, замена, пломбировка счетчиков электроэнергии:', inlines.pb_telephone('931-700'))
    
    
async def gos_check(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, 'Госпроверка приборов учетка Взлет-Кузбасс:', inlines.pb_telephone('72-36-51'))
    

async def back(callback: types.CallbackQuery, state:FSMContext):
    await utils.send_message(callback, state, 'Телефонная книга:', markup=inlines.phonebook())