from aiogram import types

menu = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton(
        "Datebook",
        "Command help",
        "Contacts",
    ),
)


planner_menu = types.ReplyKeyboardMarkup().add(
    types.KeyboardButton("Create mark", "Browse marks", "Contacts"),
)


async def menu_button_h(m: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
        *("Datebook", "Command help", "Contacts")
    )
    await m.answer("How can i help you?", reply_markup=keyboard)


async def planner_menu_h(m: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
        *("Create mark", "Browse marks", "Back to menu")
    )
    await m.answer(
        "Will we create a new datebook or will we look at the old one?",
        reply_markup=keyboard,
    )


async def cmd_list(m: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add("Back to menu")
    await m.answer(
        """
            Available commands: \n
                /help \n
                /contacts  \n
                /datebook \n
                /menu
        """,
        reply_markup=keyboard,
    )
