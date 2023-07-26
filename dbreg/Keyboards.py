from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram import types


dp = Dispatcher

async def menu_button_h(m: types.Message):
    keyboard = (
        types.ReplyKeyboardMarkup(resize_keyboard=True)
        .add(*('Datebook', 'Command help', 'Contacts'))
    )
    await m.answer('How can i help you?',reply_markup=keyboard)

async def planner_menu_h(m: types.Message):
    keyboard = (

        types.ReplyKeyboardMarkup(resize_keyboard=True)
        .add(*('Create mark', 'Browse marks', 'Back to menu'))
    ) 
    await m.answer(
        'Will we create a new datebook or will we look at the old one?', 
        reply_markup=keyboard
        )

async def cmd_list(m: types.Message):
    keyboard = (
        types.ReplyKeyboardMarkup(resize_keyboard=True)
        .add('Back to menu')
    )
    await m.answer(
        '''
            Available commands: \n
                /help \n
                /contacts  \n
                /datebook \n
                /menu
        ''',
        reply_markup=keyboard
        )

def register_handler_menu(dp: Dispatcher):
    dp.register_message_handler(
        menu_button_h, Text(equals=['Back to menu', '/menu'], ignore_case=True)
        )
    
def register_handler_planner(dp: Dispatcher):
    dp.register_message_handler(
        planner_menu_h, Text(equals=['Datebook', '/datebook'])
        )
    
def register_handler_help(dp: Dispatcher):
    dp.register_message_handler(
        cmd_list, Text(equals=['Command help', '/help'])
    )