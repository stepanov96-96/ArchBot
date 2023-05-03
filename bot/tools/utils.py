from aiogram import types
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext


async def delete_last_message(handler:types.Message|types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        last_message_id = data.get('last_msg_id')
        if last_message_id:
            await handler.bot.delete_message(handler.from_user.id, last_message_id)
            

async def send_message(handler:types.Message|types.CallbackQuery, state:FSMContext, text:str, markup:ReplyKeyboardMarkup|InlineKeyboardMarkup=None):
    await delete_last_message(handler, state)
    message = await handler.bot.send_message(handler.from_user.id, text, reply_markup=markup)
    await state.update_data(last_msg_id=message.message_id)
    

async def send_document(handler:types.Message|types.CallbackQuery, state:FSMContext, document, caption:str, markup:ReplyKeyboardMarkup|InlineKeyboardMarkup=None):
    await delete_last_message(handler, state)
    message = await handler.bot.send_document(handler.from_user.id, document=document, caption=caption, reply_markup=markup)
    await state.update_data(last_msg_id=message.message_id)