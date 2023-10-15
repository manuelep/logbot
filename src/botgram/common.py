
import sys
import logging
from . import settings

logger = logging.getLogger(settings.APP_NAME)
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)
for item in settings.LOGGERS:
    level, filename = item.split(":", 1)
    if filename in ("stdout", "stderr"):
        handler = logging.StreamHandler(getattr(sys, filename))
    else:
        handler = logging.FileHandler(filename)
    handler.setFormatter(formatter)
    logger.setLevel(getattr(logging, level.upper(), "DEBUG"))
    logger.addHandler(handler)
    
if __name__=='__main__':
    logger.debug('Just a DEBUG message')
    logger.warning("Hey! That's a WARNING!")
    logger.critical("BOOOMM!")