import keyboards


from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram import Bot, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from cfg.config_reader import config
from dbreg.dbedit import register_edit_handler
from dbreg.datebook.db import _init_db


bot = Bot(token=config.tg_bot.token)
dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup(_: Dispatcher):
    _init_db()


if __name__ == "__main__":
    from handlers import setup as setup_handlers

    setup_handlers()

    register_edit_handler(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
