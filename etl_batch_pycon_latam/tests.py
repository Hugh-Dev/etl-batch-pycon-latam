import sqlite3
import pandas as pd

# conn = sqlite3.connect('etl_batch_pycon_latam.db')
# query = "SELECT * FROM openweathermap;"
# df_resultado = pd.read_sql_query(query, conn)
# print(df_resultado)
# conn.close()

# conn = sqlite3.connect('etl_batch_pycon_latam.db')
# query = "SELECT * FROM trusted_api;"
# df_resultado = pd.read_sql_query(query, conn)
# print(df_resultado)
# conn.close()

# conn = sqlite3.connect('etl_batch_pycon_latam.db')
# query = "SELECT * FROM trusted_csv;"
# df_resultado = pd.read_sql_query(query, conn)
# print(df_resultado)
# conn.close()

conn = sqlite3.connect('etl_batch_pycon_latam.db')
query = "SELECT * FROM trusted_db;"
df_resultado = pd.read_sql_query(query, conn)
print(df_resultado)
conn.close()

# conn = sqlite3.connect('etl_batch_pycon_latam.db')
# df.to_sql('usuarios', conn, if_exists='replace', index=False)
# conn.close()

# conn = sqlite3.connect('etl_batch_pycon_latam.db')
# query = "SELECT name FROM sqlite_master WHERE type='table';"
# df_tables = pd.read_sql_query(query, conn)
# conn.close()
# print(df_tables)