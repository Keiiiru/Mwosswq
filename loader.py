from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from cfg.config_reader import config

bot = Bot(config.tg_bot.token)
dp = Dispatcher(bot, storage=MemoryStorage())
