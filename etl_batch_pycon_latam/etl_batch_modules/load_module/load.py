#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# """
# ░█░░░█▀█░█▀█░█▀▄░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀▀
# ░█░░░█░█░█▀█░█░█░░░█░█░█░█░█░█░█░█░█░░░█▀▀
# ░▀▀▀░▀▀▀░▀░▀░▀▀░░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀ ©2024 Pycon Latam
# """
# @namespace extract-module.extract
# Contains .
# @author Hugo Ramirez (hughpythoneer as X)
# Pycon Latam 2024 - Mexico

import sys
sys.path.append('etl_batch_pycon_latam')

from config.db_config import conn
from utilities.libs import pd


class loadFromDatasetApi:
    global conn

    def __init__(self) -> None:
        pass

    def load_data(self, dataframe) -> pd.DataFrame:
        # print(dataframe.dtypes)
        dataframe.to_sql('trusted_api', conn, if_exists='replace', index=False)
        # conn.close()

class loadFromDatasetCsv:

    def __init__(self) -> None:
        pass

    def load_data(self, dataframe) -> pd.DataFrame:
        # print(dataframe.dtypes)
        dataframe.to_sql('trusted_csv', conn, if_exists='replace', index=False)
        # conn.close()

class loadFromDatasetDb:

    def __init__(self) -> None:
        pass

    def load_data(self, dataframe) -> pd.DataFrame:
        # print(dataframe.dtypes)
        dataframe.to_sql('trusted_db', conn, if_exists='replace', index=False)
        # conn.close()
