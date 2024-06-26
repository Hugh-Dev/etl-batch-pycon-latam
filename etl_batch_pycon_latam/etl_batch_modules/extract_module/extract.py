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
    """
    A class to extract data from a CSV file.

    Attributes:
    -----------
    path : str
        The file path to the CSV file containing customer data.
    to_extraction : DataFrame
        A pandas DataFrame loaded from a layout CSV file specifying which columns and volumen to extract.

    Methods:
    --------
    __init__(self) -> None:
        Initializes the ExtractFromCsv class by setting the path to the customers CSV file,
        loading the layout for extraction from another CSV file, extracting the column names
        and the volume of data to be extracted.

    extract_data(self):
        Extracts data from the CSV file specified by the path attribute, using the columns
        and volume specified. Returns a pandas DataFrame containing the extracted data.
        If the file does not exist, it returns None.
    """
    def __init__(self) -> None:
        self.path = './tmp/customers.csv'
        to_extraction = pd.read_csv('./layouts/layout_to_extraction.csv')
        self.columns = to_extraction['columns'].to_list()
        self.volumen = to_extraction[to_extraction['volumen'].notna()]['volumen'].astype(int)[0]

        
    def extract_data(self):
        if os.path.isfile(self.path):
            costumers = pd.read_csv(f'{self.path}', usecols=self.columns, nrows=self.volumen, index_col=False, low_memory=True)
        return costumers

class ExtractFromDB:

    def __init__(self) -> None:
        self.conn = sqlite3.connect('etl_batch_pycon_latam.db')

    def extract_data(self):

        query = "SELECT * FROM openweathermap;"
        response = pd.read_sql_query(query, self.conn)
        self.conn.close()

        return response
