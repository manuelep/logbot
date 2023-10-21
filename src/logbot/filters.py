from .bot_utils import _start_handler, _level_handler

from typing import Any, Dict, Optional, Union

from aiogram import Router
from aiogram.filters import Filter
from aiogram.types import Message, User

router = Router(name=__name__)


class DebugLevelFilter(Filter):
    def __init__(self, name: Optional[str] = None) -> None:
        self.name = name

    async def __call__(
        self,
        message: Message,
        event_from_user: User
        # Filters also can accept keyword parameters like in handlers
    ) -> Union[bool, Dict[str, Any]]:
        if message.text.casefold() in [
            'debug', 'info', 'warning', 'error', 'critical'
        ]:
            # Returning a dictionary that will update the context data
            return {"level": message.text.casefold()}
        return False
