import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from dotenv import load_dotenv
import openai
import logging

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set OpenAI key
openai.api_key = OPENAI_API_KEY

# Bot and Dispatcher setup
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Reference class
class Reference:
    def __init__(self) -> None:
        self.response = " "

ref = Reference()

# Clear past conversation
def clear_past():
    ref.response = " "

# Start command handler
@dp.message(F.text == "/start")
async def start_command(message: types.Message):
    await message.answer("Hello! I'm your AI assistant. How can I help you today?")

# Help command
@dp.message(F.text == "/help")
async def helper(message: types.Message):
    help_command = """
/start - Start the bot and get a welcome message.
/help - Get a list of available commands.
/clear - Clear the reference and past conversation."""
    await message.reply(help_command)

# Clear command
@dp.message(F.text == "/clear")
async def clear_command(message: types.Message):
    clear_past()
    await message.reply("Reference cleared!")

# Handle general messages
@dp.message()
async def chatgpt(message: types.Message):
    print(f">>> USER:\n\t{message.text}")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": ref.response},
            {"role": "user", "content": message.text}
        ]
    )

    ref.response = response.choices[0].message.content
    print(f">>> ChatGPT:\n\t{ref.response}")
    await message.answer(ref.response)

# Main async function
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Entry point
if __name__ == '__main__':
    asyncio.run(main())
