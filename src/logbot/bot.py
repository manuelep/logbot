import asyncio
import logging
import sys
from os import getenv

from . import settings
from .common import logger

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.utils.token import TokenValidationError

from .filters import DebugLevelFilter
from .bot_utils import _start_handler, _level_handler

# Bot token can be obtained via https://t.me/BotFather
TOKEN = settings.BOT_TOKEN

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    # db.chat.insert(chat_id = message.chat.id)

    try:
        uid = _start_handler(message.chat.id)
    except Exception as err:
        await message.answer(f"Error, {err}!")
    else:
        if uid:
            await message.answer(f"Welcome, {hbold(message.from_user.full_name)}!")
        else:
            await message.answer(f"Welcome back, {hbold(message.from_user.full_name)}!")
    
@dp.message(DebugLevelFilter())
async def command_level_handler(message: Message, level: str) -> None:
    """ """
    try:
        result = _level_handler(message.chat.id, getattr(logging, level.upper()))
    except Exception as err:
        await message.answer(f"Error, {err}!")
    else:
        if result is None:
            await message.answer("No user founf to update")
        else:
            await message.answer(f"Your log level now is {level.upper()}")


# @dp.message()
# async def 

@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
    breakpoint()


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    try:
        bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    except TokenValidationError:
        logger.debug(TOKEN)
        raise
    # And the run events dispatching
    await dp.start_polling(bot)

def run() -> None:
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


if __name__ == "__main__":
    run()