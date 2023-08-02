import logging

from aiogram import Dispatcher, executor

from loader import dp
from dbreg.dbedit import register_edit_handler
from dbreg.datebook.db import init_db
from handlers import setup as setup_handlers

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(filename)s - %(message)s",
)


async def on_startup(_: Dispatcher):
    init_db()


if __name__ == "__main__":
    setup_handlers()
    register_edit_handler(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
