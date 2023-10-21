import logging
from . import settings
from .handler import BotgramHandler

FORMAT = "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"

def get_logger(name='log', level=logging.INFO, welcome=True):

    logger = logging.getLogger(name)
    handler = BotgramHandler()
    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)

    logger.setLevel(level)
    logger.addHandler(handler)
    if welcome:
        handler.send_start_message(level)
    return logger