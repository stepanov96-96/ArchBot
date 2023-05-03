from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScope

async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('start', 'Начать общение с ботом'),
            BotCommand('add_project', 'Добавить проект'),
            BotCommand('delete_project', 'Удалить проект'),
        ],
        scope=BotCommandScopeDefault()
    )