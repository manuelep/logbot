from .common import logger
from .models import db


def _start_handler(chat_id: int) -> int:
    """ """
    uid = None
    try:
        uid = db.chat.update_or_insert(chat_id=chat_id)
    except Exception as err:
        db.rollback()
        raise
    else:
        db.commit()
    return uid

def _level_handler(chat_id: int, debug_level: int) -> None:
    rec = db.chat(chat_id=chat_id)
    if rec is None:
        return None
    try:
        rec.update_record(level = debug_level)
    except Exception as err:
        db.rollback()
        raise
    else:
        db.commit()
        return rec.id