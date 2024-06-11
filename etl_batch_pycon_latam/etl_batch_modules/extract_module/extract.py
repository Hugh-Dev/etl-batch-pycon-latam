#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# """
# ░█▀▀░█░█░▀█▀░█▀▄░█▀█░█▀▀░▀█▀░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀▀
# ░█▀▀░▄▀▄░░█░░█▀▄░█▀█░█░░░░█░░░░█░█░█░█░█░█░█░█░█░░░█▀▀
# ░▀▀▀░▀░▀░░▀░░▀░▀░▀░▀░▀▀▀░░▀░░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀  ©2024 Pycon Latam
# """
# @namespace extract-module.extract
# Contains .
# @author Hugo Ramirez (@hughpythoneer as X)
# Pycon Latam 2024 - Mexico



import sys
sys.path.append('etl_batch_pycon_latam')
from config.settings import URL_API
from utilities.libs import np, pd, requests, os, sqlite3

class ExtractFromApi:
    def __init__(self, n, api_key) -> None:
        self.base_url = f"{URL_API}"
        self.api_key = api_key
        self.latitudes = np.random.uniform(low=-90.0, high=90.0, size=n)
        self.longitudes = np.random.uniform(low=-180.0, high=180.0, size=n)

    def extract_data(self):
        weather_data = []
        for lat, lon in zip(self.latitudes, self.longitudes):
            params = {'lat': lat, 'lon': lon, 'appid': self.api_key}
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                weather_data.append(response.json())
            else:
                print(f"Error lat={lat}, lon={lon}")
        return weather_data
    
class ExtractFromCsv:

    def __init__(self) -> None:
        self.path = './tmp/layout_global_temperatures.csv'
        
    def extract_data(self):

        if os.path.isfile(self.path):
            global_temperatures = pd.read_csv(f'{self.path}', index_col=False, low_memory=True)

        return global_temperatures

class ExtractFromDB:

    def __init__(self) -> None:
        self.conn = sqlite3.connect('etl_batch_pycon_latam.db')

    def extract_data(self):

        query = "SELECT * FROM openweathermap;"
        response = pd.read_sql_query(query, self.conn)
        self.conn.close()

        return response
