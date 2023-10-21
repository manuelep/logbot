import asyncio
import logging
from . import settings
from .common import logger

from .models import db
from aiogram.methods import SendMessage
from aiogram import Bot

loop = asyncio.get_event_loop()

class BotgramHandler(logging.Handler):
    """ """
    
    def __init__(self):
        logging.Handler.__init__(self)
        self.bot = Bot(settings.BOT_TOKEN)

    async def _send_start_message(self, level:int) -> None:
        """ """
        message = f"🏁 Logging started with level {logging.getLevelName(level)} 🏁"
        chats = db(db.chat).select()
        await asyncio.gather(*[self.bot.send_message(chat.chat_id, message) for chat in chats])
        

    async def send_message(self, message, level):
        chats = db(db.chat.level<=level).select()
        logger.debug(message)
        logger.debug(len(chats))
        
        # await self.bot.send_message(197800374, message)
        await asyncio.gather(*[self.bot.send_message(chat.chat_id, message) for chat in chats])

    def send_start_message(self, level: int) -> None:
        loop.run_until_complete(self._send_start_message(level))

    def emit(self, record):
        """ """        
        message = self.format(record)
        # loop = asyncio.get_event_loop()
        loop.run_until_complete(self.send_message(message, record.levelno))
        

