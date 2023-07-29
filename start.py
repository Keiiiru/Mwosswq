import keyboards


from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from cfg.config_reader import config
from dbreg.dbedit import register_edit_handler
from dbreg.datebook.db import _init_db


bot = Bot(token=config.tg_bot.token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start", "начать"])
async def cmd_start(message: types.Message):
    await message.answer("Hey?\n How can I help you?", reply_markup=keyboards.menu)


@dp.message_handler(commands=["contacts"])
async def buttons(m: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [types.InlineKeyboardButton(text="", url="")]
    keyboard.add(*buttons)
    await m.answer("Contacts:", reply_markup=keyboard)


async def on_startup(_: Dispatcher):
    _init_db()


if __name__ == "__main__":
    register_edit_handler(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
