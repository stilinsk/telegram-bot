import logging
import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Logging
logging.basicConfig(level=logging.INFO)

# Create bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Handlers
@dp.message(F.text.in_(['/start', '/help']))
async def send_welcome(message: Message):
    await message.answer("Hello! 👋\nI'm your echo bot.\nPowered by aiogram 3.")

# Main async function
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Entry point
if __name__ == '__main__':
    asyncio.run(main())
