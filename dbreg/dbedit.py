from aiogram import Dispatcher,types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from dbreg.datebook.db import add_mark, get_marks


class AddMark(StatesGroup):
    Day_of_week = State()
    Activity_for_the_day = State()

async def get_day_handler(m: types.Message, state: FSMContext):
    keyboard = (
        types.ReplyKeyboardMarkup(resize_keyboard=True)
        .add(*(
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
        'Back to menu'
        ))
    )
    await m.answer('Choose the day of week',reply_markup=keyboard)
    await AddMark.Day_of_week.set()

async def get_activity_handler(m: types.Message, state: FSMContext):
    await state.update_data(Day_of_week = m.text)
    data = await state.get_data()
    await m.answer('Write your activity')
    await AddMark.Activity_for_the_day.set()

async def add_mark_handler(m: types.Message, state: FSMContext):
    await state.update_data(Activity_for_the_day = m.text)
    data = await state.get_data()
    add_mark(data["Day_of_week"], data["Activity_for_the_day"], m.from_user.id)
    keyboard = (
        types.ReplyKeyboardMarkup(resize_keyboard=True)
        .add(*('Return to create mark','Browse marks','Back to menu'))
    )
    await m.answer('Mark has been added', reply_markup=keyboard)
    await state.finish()

async def get_mark_handler(m: types.Message):
    message = ""
    for row in get_marks(m.from_id):
        message += f"Day: {row[1]}, activity: {row[2]}\n"
    await m.answer(message)

def register_edit_handler(dp: Dispatcher):
    dp.register_message_handler(
        get_day_handler,Text(equals=['Create mark', 'Return to create mark']), state='*'
    )
    dp.register_message_handler(
        get_activity_handler, state=AddMark.Day_of_week
    )
    dp.register_message_handler(
        add_mark_handler, state= AddMark.Activity_for_the_day
    )
    dp.register_message_handler(
        get_mark_handler, Text(equals=['Browse marks'])
    )