import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN


# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not BOT_TOKEN:
    exit("No token provided")

# init
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
