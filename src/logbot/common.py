
import sys
import logging
from pydal import DAL
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

# #######################################################
# connect to db
# #######################################################

# logger.debug(settings.DB_URI)

db = DAL(
    settings.DB_URI,
    folder=settings.DB_FOLDER,
    pool_size=settings.DB_POOL_SIZE,
    migrate=settings.DB_MIGRATE,
    fake_migrate=settings.DB_FAKE_MIGRATE,
)

if __name__=='__main__':
    logger.debug('Just a DEBUG message')
    logger.warning("Hey! That's a WARNING!")
    logger.critical("BOOOMM!")