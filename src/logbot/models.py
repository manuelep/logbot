"""
This file defines the database models
"""
from pydal import Field
from .common import db
from pydal.validators import *
import logging

### Define your table below
#

db.define_table('chat',
    Field('chat_id', 'integer', unique=True, notnull=True),
    Field('level', 'integer', notnull=True, default=logging.INFO)
)

# always commit your models to avoid problems later

db.commit()
#
