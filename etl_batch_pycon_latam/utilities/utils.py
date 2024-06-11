# """
# ░█░█░▀█▀░▀█▀░█░░░▀█▀░▀█▀░▀█▀░█▀▀░█▀▀
# ░█░█░░█░░░█░░█░░░░█░░░█░░░█░░█▀▀░▀▀█
# ░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀
# """

import sys
sys.path.append('etl_batch_pycon_latam')

from utilities.libs import time, PrettyTable

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"The function '{func.__name__}' took {total_time} seconds to execute.")
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