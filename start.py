from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from cfg.config_reader import config
from dbreg.keyboards import register_handler_menu, register_handler_planner, register_handler_help
from dbreg.dbedit import register_edit_handler
from dbreg.datebook.db import _init_db


bot = Bot(token = config.tg_bot.token)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start','начать'])
async def cmd_start(message: types.Message):
    keyboard = (
        types.ReplyKeyboardMarkup(resize_keyboard=True)
        .add(*('Datebook', 'Command help', 'Contacts'))
    )
    await message.answer('Hey?\n How can I help you?', reply_markup=keyboard)

@dp.message_handler(commands=['contacts'])
async def buttons(m: types.Message):
    keyboard = (
        types.InlineKeyboardMarkup(row_width= 1)
    )
    buttons = [
        types.InlineKeyboardButton(text='', url='')
    ]
    keyboard.add(*buttons)
    await m.answer('Contacts:', reply_markup=keyboard)

async def on_startup(_: Dispatcher):
    _init_db()

if __name__ == '__main__':
    register_handler_menu(dp)
    register_handler_planner(dp)
    register_handler_help(dp)
    register_edit_handler(dp)

    executor.start_polling(
        dp, skip_updates=True, on_startup=on_startup
        )
