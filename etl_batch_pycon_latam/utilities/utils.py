# """
# ░█░█░▀█▀░▀█▀░█░░░▀█▀░▀█▀░▀█▀░█▀▀░█▀▀
# ░█░█░░█░░░█░░█░░░░█░░░█░░░█░░█▀▀░▀▀█
# ░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀
# """

import sys
sys.path.append('etl_batch_pycon_latam')

from utilities.libs import time, PrettyTable, Polygon, wkt

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"The function '{func.__name__}' took {total_time} seconds to execute. ⏳")
        return result
    return wrapper

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def dataframe_a_prettytable(df, n_rows=None):

    table = PrettyTable()
    table.field_names = df.columns.tolist()
    df_limited = df.iloc[:n_rows] if n_rows is not None else df
    for index, row in df_limited.iterrows():
        table.add_row(row.tolist())
    
    return table

def create_polygon_from_coords(lon, lat):
    return Polygon([(lon, lat), (lon, lat + 0.1), (lon + 0.1, lat + 0.1), (lon + 0.1, lat), (lon, lat)])

def safe_wkt_load(polygon):
    if isinstance(polygon, Polygon):
        return polygon
    else:
        return wkt.loads(polygon)

def round_polygon(polygon_wkt, precision=2):
    polygon = wkt.loads(polygon_wkt)
    rounded_coordinates = []
    for x, y in polygon.exterior.coords:
        rounded_coordinates.append((round(x, precision), round(y, precision)))
    rounded_polygon = Polygon(rounded_coordinates)
    return rounded_polygon.wkt