import config
from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

def register_handlers():
    from .handlers import commands, init_user_info, phonebook, debt, shedule, testimony, orders, paylist
    commands.register_handlers(dp)
    init_user_info.register_handlers(dp)
    phonebook.register_handlers(dp)
    debt.register_handlers(dp)
    shedule.register_handlers(dp)
    testimony.register_handlers(dp)
    orders.register_handlers(dp)
    paylist.register_handlers(dp)

def start_bot():
    register_handlers()
    executor.start_polling(dp, skip_updates=True)