import os
from pathlib import Path
from .tools import required_folder
# import logging

# db settings
APP_FOLDER = Path(__file__).parent
APP_NAME = APP_FOLDER.parent.parent.name
# DB_FOLDER:    Sets the place where migration files will be created
#               and is the store location for SQLite databases
DB_FOLDER = required_folder(Path(), "databases")

DBNET = os.environ.get('DBNET')
DBUSERNAME = os.environ.get('DBUSERNAME')
DBUSERPASSWORD = os.environ.get('DBUSERPASSWORD')
DBPORT = os.environ.get('DBPORT')
DBNAME = os.environ.get('DBNAME')

DB_URI = f"postgres://{DBUSERNAME}:{DBUSERPASSWORD}@{DBNET}:{DBPORT}/{DBNAME}"

DB_POOL_SIZE = 1
DB_MIGRATE = os.environ.get('DB_MIGRATE', 'False')=='True'
DB_FAKE_MIGRATE = False  # maybe?

# logger settings
# This should be in a separate settings file

LOGGERS = [
    "debug:stdout"
]  # syntax "severity:filename" filename can be stderr or stdout

BOT_TOKEN = os.environ.get('BOT_TOKEN')

# DEFAULT_LOG_LEVEL = logging.WARNING

# try import private settings
try:
    from .settings_private import *
except (ImportError, ModuleNotFoundError):
    pass