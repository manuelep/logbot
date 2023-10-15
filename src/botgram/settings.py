import os

# logger settings
# This should be in a separate settings file

APP_NAME = 'botgram'

LOGGERS = [
    "debug:stdout"
]  # syntax "severity:filename" filename can be stderr or stdout

BOT_TOKEN = os.environ.get('BOT_TOKEN')

# try import private settings
try:
    from .settings_private import *
except (ImportError, ModuleNotFoundError):
    pass