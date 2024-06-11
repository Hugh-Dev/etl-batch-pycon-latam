import sqlite3
import pandas as pd

# Conectar a la base de datos
conn = sqlite3.connect('etl_batch_pycon_latam.db')

# Realizar una consulta SELECT para recuperar datos
query = "SELECT * FROM openweathermap;"
df_resultado = pd.read_sql_query(query, conn)

# Imprimir los resultados
print(df_resultado)

# Cerrar la conexión
conn.close()