# """
# ░█░░░▀█▀░█▀▄░█▀▄░█▀█░█▀▄░█░█
# ░█░░░░█░░█▀▄░█▀▄░█▀█░█▀▄░░█░
# ░▀▀▀░▀▀▀░▀▀░░▀░▀░▀░▀░▀░▀░░▀░
# """

from decouple import config
from prettytable import PrettyTable
from shapely.geometry import Polygon
# import geopandas as gpd
from shapely import wkt
import json
import sqlite3
import requests
import pandas as pd
import numpy as np
import time
import os
