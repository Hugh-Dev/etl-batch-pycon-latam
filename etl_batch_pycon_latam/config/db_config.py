# """
# ░█▀▀░▄▀▄░█░░░▀█▀░▀█▀░█▀▀░▀▀█
# ░▀▀█░█\█░█░░░░█░░░█░░█▀▀░░▀▄
# ░▀▀▀░░▀\░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀░ 
# """

import sys
sys.path.append('etl_batch_pycon_latam')

from .settings import DB_NAME
from utilities.libs import sqlite3

conn = sqlite3.connect('etl_batch_pycon_latam.db')