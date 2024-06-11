#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# """
# ░▀█▀░█▀▄░█▀█░█▀█░█▀▀░█▀▀░█▀█░█▀▄░█▄█░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀▀
# ░░█░░█▀▄░█▀█░█░█░▀▀█░█▀▀░█░█░█▀▄░█░█░░░█░█░█░█░█░█░█░█░█░░░█▀▀ 
# ░░▀░░▀░▀░▀░▀░▀░▀░▀▀▀░▀░░░▀▀▀░▀░▀░▀░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀ ©2024 Pycon Latam
# """
# @namespace 
# Contains 
# @author Hugo Ramirez (hughpythoneer as X)
# Pycon Latam 2024 - Mexico

import sys
sys.path.append('etl_batch_pycon_latam')

from utilities.libs import pd
from utilities.utils import kelvin_a_celsius


class TransformToApi:

    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon

    def transform_data(self, weather_data) -> list:

        try:
            df_weather = pd.DataFrame(weather_data)
            coord_df = pd.json_normalize(df_weather['coord'].apply(pd.Series)).add_prefix('coord_')
            df_weather = pd.concat([df_weather.drop(columns=['coord']), coord_df], axis=1)

            weather_df = pd.json_normalize(df_weather['weather'].apply(lambda x: x[0] if x else {})).add_prefix('weather_')
            df_weather = pd.concat([df_weather.drop(columns=['weather']), weather_df], axis=1)

            main_df = pd.json_normalize(df_weather['main']).add_prefix('main_')
            wind_df = pd.json_normalize(df_weather['wind']).add_prefix('wind_')
            clouds_df = pd.json_normalize(df_weather['clouds']).add_prefix('clouds_')
            sys_df = pd.json_normalize(df_weather['sys']).add_prefix('sys_')

            df_weather = pd.concat([df_weather.drop(columns=['main', 'wind', 'clouds', 'sys']), main_df, wind_df, clouds_df, sys_df], axis=1)
            
            df_weather['lat'] = self.lat
            df_weather['lon'] = self.lon
            
            df_weather = df_weather.loc[df_weather['name'] != ''][['name', 'lat', 'lon', 'main_temp_min', 'main_temp_max', 'sys_country']]
            
            df_weather['celsius_temp_min'] = df_weather['main_temp_min'].apply(kelvin_a_celsius)
            df_weather['celsius_temp_max'] = df_weather['main_temp_max'].apply(kelvin_a_celsius)

            response = (
                df_weather
                .filter(['name', 'lat', 'lon', 'sys_country'])
            )

            return response
        
        except Exception as e:
            raise Exception("log", e)

class TransformToCsv:

    def __init__(self) -> None:
        pass

    def transform_data(self, dataframe) -> pd.DataFrame:
        self.dataframe = dataframe

        self.dataframe['celsius_temp_min'] = pd.to_numeric(self.dataframe['celsius_temp_min'], errors='coerce')
        self.dataframe['celsius_temp_max'] = pd.to_numeric(self.dataframe['celsius_temp_max'], errors='coerce')

        self.response = self.dataframe.groupby('sys_country').agg(
            temp_min_promedio=('celsius_temp_min', 'mean'),
            temp_max_promedio=('celsius_temp_max', 'mean')
        ).reset_index()

        self.response['temp_min_promedio'] = self.response['temp_min_promedio'].round(2)
        self.response['temp_max_promedio'] = self.response['temp_max_promedio'].round(2)

        return self.response

class TransformToDb:

    def __init__(self) -> None:
        pass

    def transform_data(self, dataframe) -> pd.DataFrame:
        self.dataframe = dataframe

        # response = (
        #     self.dataframe
        #     .filter([

        #     ])
        # )
        
        return self.dataframe