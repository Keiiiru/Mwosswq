import keyboards


from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler(commands=["start", "начать"])
async def cmd_start(message: types.Message):
    await message.answer("Hey?\n How can I help you?", reply_markup=keyboards.menu)


@dp.message_handler(Text(equals="Contacts"))
async def buttons(m: types.Message):
    await m.answer("Contacts:", reply_markup=keyboards.contacts)


@dp.message_handler(Text(equals="Command help"))
async def cmd_list(m: types.Message):
    await m.answer(
        """
        available commands: \n

        """,
        reply_markup=keyboards.cmd_list,
    )


@dp.message_handler(Text(equals="Back to menu"))
async def menu(m: types.Message):
    await m.answer("Hey?\n How can I help you?", reply_markup=keyboards.menu)


@dp.message_handler(Text(equals="Datebook"))
async def datebook(m: types.Message):
    await m.answer(
        "Will we create a new mark or browse old one?",
        reply_markup=keyboards.planner_menu,
    )
