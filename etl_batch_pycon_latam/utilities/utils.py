# """
# ░█░█░▀█▀░▀█▀░█░░░▀█▀░▀█▀░▀█▀░█▀▀░█▀▀
# ░█░█░░█░░░█░░█░░░░█░░░█░░░█░░█▀▀░▀▀█
# ░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀
# """

import sys
sys.path.append('etl_batch_pycon_latam')

from utilities.libs import time, PrettyTable, Polygon, wkt

"""
ETL Utilities Module
--------------------

This module contains various utility functions for use in ETL processes.

Functions:
- timer(func): Decorator to measure the execution time of a function.
- kelvin_a_celsius(kelvin): Convert temperature from Kelvin to Celsius.
- dataframe_a_prettytable(df, n_rows=None): Convert a pandas DataFrame to a PrettyTable.
- create_polygon_from_coords(lon, lat): Create a Polygon object from longitude and latitude.
- safe_wkt_load(polygon): Safely load a WKT string into a Polygon object.
- round_polygon(polygon_wkt, precision=2): Round the coordinates of a polygon to a specified precision.
"""

import sys
sys.path.append('etl_batch_pycon_latam')

from utilities.libs import time, PrettyTable, Polygon, wkt

def timer(func):
    """
    Decorator to measure the execution time of a function.
    
    Args:
        func (callable): The function to be timed.
    
    Returns:
        callable: The wrapped function that prints the execution time.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"The function '{func.__name__}' took {total_time} seconds to execute. ⏳")
        return result
    return wrapper

def kelvin_a_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.
    
    Args:
        kelvin (float): Temperature in Kelvin.
    
    Returns:
        float: Temperature in Celsius.
    """
    return kelvin - 273.15

def dataframe_a_prettytable(df, n_rows=None):
    """
    Convert a pandas DataFrame to a PrettyTable.
    
    Args:
        df (pandas.DataFrame): The DataFrame to be converted.
        n_rows (int, optional): Number of rows to include in the table. Defaults to None, which includes all rows.
    
    Returns:
        PrettyTable: The resulting PrettyTable object.
    """
    table = PrettyTable()
    table.field_names = df.columns.tolist()
    df_limited = df.iloc[:n_rows] if n_rows is not None else df
    for index, row in df_limited.iterrows():
        table.add_row(row.tolist())
    
    return table

def create_polygon_from_coords(lon, lat):
    """
    Create a Polygon object from longitude and latitude.
    
    Args:
        lon (float): Longitude.
        lat (float): Latitude.
    
    Returns:
        Polygon: The resulting Polygon object.
    """
    return Polygon([(lon, lat), (lon, lat + 0.1), (lon + 0.1, lat + 0.1), (lon + 0.1, lat), (lon, lat)])

def safe_wkt_load(polygon):
    """
    Safely load a WKT string into a Polygon object.
    
    Args:
        polygon (str or Polygon): The WKT string or Polygon object.
    
    Returns:
        Polygon: The resulting Polygon object.
    """
    if isinstance(polygon, Polygon):
        return polygon
    else:
        return wkt.loads(polygon)

def round_polygon(polygon_wkt, precision=2):
    """
    Round the coordinates of a polygon to a specified precision.
    
    Args:
        polygon_wkt (str): The WKT string of the polygon.
        precision (int, optional): The number of decimal places to round to. Defaults to 2.
    
    Returns:
        str: The WKT string of the rounded polygon.
    """
    polygon = wkt.loads(polygon_wkt)
    rounded_coordinates = []
    for x, y in polygon.exterior.coords:
        rounded_coordinates.append((round(x, precision), round(y, precision)))
    rounded_polygon = Polygon(rounded_coordinates)
    return rounded_polygon.wkt
