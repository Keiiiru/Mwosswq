from aiogram import types

menu = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton("Datebook"),
    types.KeyboardButton("Command help"),
    types.KeyboardButton("Contacts"),
)


planner_menu = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton("Create mark"),
    types.KeyboardButton("browse marks"),
    types.KeyboardButton("Back to menu"),
)


cmd_list = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    types.KeyboardButton("Back to menu"),
)


contacts = types.InlineKeyboardMarkup(row_width=1).add(
    types.InlineKeyboardButton(text="Developer", url="https://t.me/Mwossw")
)
