#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# """
# ░▀█▀░█▀▄░█▀█░█▀█░█▀▀░█▀▀░█▀█░█▀▄░█▄█░░░█▄█░█▀█░█▀▄░█░█░█░░░█▀▀
# ░░█░░█▀▄░█▀█░█░█░▀▀█░█▀▀░█░█░█▀▄░█░█░░░█░█░█░█░█░█░█░█░█░░░█▀▀ 
# ░░▀░░▀░▀░▀░▀░▀░▀░▀▀▀░▀░░░▀▀▀░▀░▀░▀░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀ ©2024 Pycon Latam
# """
# @namespace 
# Contains This module contains classes for transforming weather data for different purposes such as API responses, CSV files, and database storage.
# @author Hugo Ramirez (hughpythoneer as X)
# Pycon Latam 2024 - Mexico

import sys
sys.path.append('etl_batch_pycon_latam')

from utilities.libs import pd, Polygon, gpd, wkt, json
from utilities.utils import kelvin_a_celsius, create_polygon_from_coords, round_polygon, safe_wkt_load


class TransformToApi:

    """
    Class to transform weather data for API response.
    
    Methods:
    - transform_data(weather_data): Transforms weather data into a structured format for API response.
    
    Attributes:
    - lat (float): Latitude coordinate.
    - lon (float): Longitude coordinate.
    """

    def __init__(self, lat, lon) -> None:
        """
        Initializes the TransformToApi instance with latitude and longitude.
        
        Args:
            lat (float): Latitude coordinate.
            lon (float): Longitude coordinate.
        """
        self.lat = lat
        self.lon = lon

    def transform_data(self, weather_data) -> list:
        """
        Transforms weather data into a structured format for API response.
        
        Args:
            weather_data (list): Raw weather data.
        
        Returns:
            list: Transformed weather data.
        
        Raises:
            Exception: If an error occurs during data transformation.
        """
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
                .astype({
                    'name': 'str',
                    'sys_country': 'str'

                })
            )
       
            return response
        
        except Exception as e:
            raise Exception("log", e)

class TransformToCsv:

    """
    Class to transform weather data for CSV output.
    
    Methods:
    - transform_data(dataframe): Transforms weather data into a format suitable for CSV output.
    """

    def __init__(self) -> None:
        """
        Initializes the TransformToCsv instance.
        """
        pass

    def transform_data(self, dataframe) -> pd.DataFrame:
        """
        Transforms weather data into a format suitable for CSV output.
        
        Args:
            dataframe (pd.DataFrame): DataFrame containing the weather data.
        
        Returns:
            pd.DataFrame: Transformed DataFrame suitable for CSV output.
        """
        dataframe['celsius_temp_min'] = pd.to_numeric(dataframe['celsius_temp_min'], errors='coerce')
        dataframe['celsius_temp_max'] = pd.to_numeric(dataframe['celsius_temp_max'], errors='coerce')

        response = dataframe.groupby('sys_country').agg(
            temp_min_promedio=('celsius_temp_min', 'mean'),
            temp_max_promedio=('celsius_temp_max', 'mean')
        ).reset_index()

        response['temp_min_promedio'] = response['temp_min_promedio'].round(2)
        response['temp_max_promedio'] = response['temp_max_promedio'].round(2)

        return response

class TransformToDb:
    """
    Class to transform weather data for database storage.
    
    Methods:
    - transform_data(dataframe): Transforms weather data into a format suitable for database storage.
    """

    def __init__(self) -> None:
        """
        Initializes the TransformToDb instance.
        """
        pass

    def transform_data(self, dataframe) -> pd.DataFrame:
        """
        Transforms weather data into a format suitable for database storage.
        
        Args:
            dataframe (pd.DataFrame): DataFrame containing the weather data.
        
        Returns:
            pd.DataFrame: Transformed DataFrame suitable for database storage.
        """
        dataframe = dataframe[dataframe['name'] != '']

        dataframe = (
            dataframe
            .filter([
                'name',
                'sys_country',
                'lat',
                'lon'
            ])
            .rename(columns={
                'lat':'latitude',
                'lon':'longitude'
            })
        )
        dataframe[['latitude', 'longitude']] = dataframe[['latitude', 'longitude']].round(2)
        dataframe['polygon'] = dataframe.apply(lambda row: create_polygon_from_coords(row['longitude'], row['latitude']), axis=1)
        dataframe['polygon'] = dataframe['polygon'].apply(safe_wkt_load)
        dataframe['polygon'] = dataframe['polygon'].astype(str)
        
        return dataframe