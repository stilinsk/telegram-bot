# telegram-bot
Sure! Here's the **line-by-line explanation of code blocks** for both files.

---

## ✅ First File (Basic Echo Bot)

```python
import logging                   # Enables logging to monitor events and errors
import os                        # Allows interaction with the operating system
import asyncio                   # Enables writing asynchronous code
from aiogram import Bot, Dispatcher, types, F  # Imports classes from aiogram for bot creation
from aiogram.types import Message              # Imports the Message type
from dotenv import load_dotenv   # Loads environment variables from a .env file
```

```python
load_dotenv()                   # Loads environment variables from the .env file
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Gets the bot token from environment
```

```python
logging.basicConfig(level=logging.INFO)  # Sets up logging with INFO level
```

```python
bot = Bot(token=TELEGRAM_BOT_TOKEN)     # Creates the bot with the token
dp = Dispatcher()                       # Initializes the dispatcher
```

```python
@dp.message(F.text.in_(['/start', '/help']))  # Handler for /start or /help command
async def send_welcome(message: Message):     # Async function to send welcome message
    await message.answer("Hello! 👋\nI'm your echo bot.\nPowered by aiogram 3.")  # Reply message
```

```python
async def main():                             # Defines the main asynchronous function
    await bot.delete_webhook(drop_pending_updates=True)  # Clears pending updates
    await dp.start_polling(bot)               # Starts polling to listen for messages
```

```python
if __name__ == '__main__':       # Runs the main function when script is executed
    asyncio.run(main())          # Executes the async main function
```

---

## ✅ Second File (`main.py` with GPT Integration)

```python
import os                         # For accessing environment variables
import asyncio                    # To handle async operations
from aiogram import Bot, Dispatcher, types, F  # Bot framework
from dotenv import load_dotenv    # Load environment variables
import openai                     # OpenAI library to access GPT
import logging                    # For logging events
```

```python
load_dotenv()                     # Load variables from .env file
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Get Telegram bot token
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")          # Get OpenAI API key
```

```python
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO
```

```python
openai.api_key = OPENAI_API_KEY    # Set OpenAI API key
```

```python
bot = Bot(token=TELEGRAM_BOT_TOKEN)  # Create Telegram bot
dp = Dispatcher()                    # Initialize dispatcher
```

```python
class Reference:                     # Class to store conversation reference
    def __init__(self) -> None:      # Constructor method
        self.response = " "          # Initialize response as empty
```

```python
ref = Reference()                    # Create Reference object
```

```python
def clear_past():                    # Function to clear past conversation
    ref.response = " "               # Reset stored response
```

```python
@dp.message(F.text == "/start")     # Handler for /start command
async def start_command(message: types.Message):  # Async function to handle it
    await message.answer("Hello! I'm your AI assistant. How can I help you today?")  # Reply
```

```python
@dp.message(F.text == "/help")      # Handler for /help command
async def helper(message: types.Message):  # Async help handler
    help_command = """
/start - Start the bot and get a welcome message.
/help - Get a list of available commands.
/clear - Clear the reference and past conversation."""  # Help text
    await message.reply(help_command)  # Send help text
```

```python
@dp.message(F.text == "/clear")     # Handler for /clear command
async def clear_command(message: types.Message):  # Async clear handler
    clear_past()                    # Clear stored response
    await message.reply("Reference cleared!")  # Acknowledge clear
```

```python
@dp.message()                       # Handler for all other messages
async def chatgpt(message: types.Message):  # Async function for GPT response
    print(f">>> USER:\n\t{message.text}")   # Print user input

    response = openai.ChatCompletion.create(  # Create GPT chat completion
        model="gpt-3.5-turbo",                # Specify model
        messages=[                            # Provide messages for context
            {"role": "assistant", "content": ref.response},  # Last assistant response
            {"role": "user", "content": message.text}         # Current user message
        ]
    )
```

```python
    ref.response = response.choices[0].message.content  # Store GPT response
    print(f">>> ChatGPT:\n\t{ref.response}")            # Print GPT response
    await message.answer(ref.response)                  # Send response to user
```

```python
async def main():                           # Define async main function
    await bot.delete_webhook(drop_pending_updates=True)  # Clear pending updates
    await dp.start_polling(bot)            # Start polling to listen for messages
```

```python
if __name__ == '__main__':                 # Run if script is main program
    asyncio.run(main())                    # Run the async main function
```

