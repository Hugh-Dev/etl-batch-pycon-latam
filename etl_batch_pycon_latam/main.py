#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# """
# ░█▀█░█░█░█▀▀░█▀█░█▀█░░░█░░░█▀█░▀█▀░█▀█░█▄█░
# ░█▀▀░░█░░█░░░█░█░█░█░░░█░░░█▀█░░█░░█▀█░█░█░
# ░▀░░░░▀░░▀▀▀░▀▀▀░▀░▀░░░▀▀▀░▀░▀░░▀░░▀░▀░▀░▀░ ©2024 Pycon Latam. Todos los derechos reservados.
# """
# @namespace etl_batch_pycon_latam.main
# Contains 
# @author Hugo Ramirez (hughpythoneer as X)
# Pycon Latam 2024 - Mexico


import sys
sys.path.append('etl_batch_pycon_latam')

from etl_batch_modules.extract_module.extract import *
from etl_batch_modules.transform_module.transform import *
from etl_batch_modules.load_module.load import *
from config.settings import API_KEY, N_REQUEST
from utilities.utils import timer, dataframe_a_prettytable


@timer
def main():
    # Initialize data pipeline... 🐍​
    try:

        banner = """

          ,---- [ Module ]
          | Extraction Layouts Excute
          `----------------------
        
        """
        print(banner)
        
        # From API
        # n_requests = int(N_REQUEST)
        # appid = f'{API_KEY}'
        # extractor_api = ExtractFromApi(n=n_requests, api_key=appid)
        # weather_data = extractor_api.extract_data()
        # lat = extractor_api.latitudes
        # lon = extractor_api.longitudes

        # From CSV
        extractor_csv = ExtractFromCsv()
        customers = extractor_csv.extract_data()
        print(customers)

        # From Data Base
        # extractor_db = ExtractFromDB()
        # openweathermap = extractor_db.extract_data()


        banner = """

          ,---- [ Module ]
          | Transformation Layouts Excute
          `----------------------
        
        """
        print(banner)

        # To API
        # transformation_api = TransformToApi(lat, lon)
        # data_response = transformation_api.transform_data(weather_data)
        # print('API OpenWeather: 📦')
        # prettytable_data_response = dataframe_a_prettytable(data_response, 5)
        # print(prettytable_data_response)

        print('\n')

        # To CSV
        transformation_csv = TransformToCsv()
        layout_customers = transformation_csv.transform_data(customers)
        # print('Customers: 📦')
        # prettytable_customers = dataframe_a_prettytable(customers, 5)
        # print(prettytable_customers)

        # To Data Base
        # transformation_db = TransformToDb()
        # openweathermap = transformation_db.transform_data(openweathermap)
        # print('Openweathermap polygon: 📦')
        # prettytable_openweathermap = dataframe_a_prettytable(openweathermap, 5)
        # print(prettytable_openweathermap)

        print('\n')

        banner = """

          ,---- [ Module ]
          | Load Layouts Excute
          `----------------------
        
        """
        print(banner)

        # Load api rest data
        # load_api = loadFromDatasetApi()
        # load_api.load_data(data_response)
        # print('successful load api data...✅')

        # Load CSV data
        # load_csv = loadFromDatasetCsv()
        # load_csv.load_data(global_temperatures)
        # print('successful load csv data...✅')

        # Load DB data
        # load_db = loadFromDatasetDb()
        # load_db.load_data(openweathermap)
        # print('successful load db data...✅')

        print('\n')
        
    except Exception as e:
        raise Exception("log", e)


if __name__ == '__main__':
    main()