# import dash
# from dash import dcc
# from dash import html
# import plotly.express as px
# import pandas as pd

# external_stylesheets = ['https://fonts.googleapis.com/css2?family=Ubuntu:wght@400;700&display=swap']

# # Crear un DataFrame de ejemplo
# df = pd.DataFrame({
#     "Frutas": ["Manzanas", "Naranjas", "Plátanos", "Mangos", "Cerezas"],
#     "Cantidad": [4, 1, 2, 2, 4]
# })

# # Crear una figura con Plotly Express
# fig = px.bar(df, x="Frutas", y="Cantidad", title="Cantidad de Frutas")

# # Iniciar la aplicación Dash
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# # Definir el layout de la aplicación
# app.layout = html.Div(children=[
#     html.H1(children='Hola Dash', style={'font-family': 'Ubuntu'}),
#     html.Div(children='''Dash: Una aplicación web para Python.''', style={'font-family': 'Ubuntu'}),
#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

# # Correr el servidor
# if __name__ == '__main__':
#     app.run_server(debug=True, port=8080)

import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://fonts.googleapis.com/css2?family=Ubuntu:wght@400;700&display=swap']

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    "Frutas": ["Manzanas", "Naranjas", "Plátanos", "Mangos", "Cerezas"],
    "Cantidad": [4, 1, 2, 2, 4]
})

# Crear figuras con Plotly Express
fig = px.bar(df, x="Frutas", y="Cantidad", title="Cantidad de Frutas")
fig2 = px.line(df, x="Frutas", y="Cantidad", title="Cantidad de Frutas (Línea)")
fig3 = px.scatter(df, x="Frutas", y="Cantidad", size="Cantidad", title="Cantidad de Frutas (Dispersión)")
fig4 = px.pie(df, names="Frutas", values="Cantidad", title="Distribución de Frutas")

# Iniciar la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Definir el layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Dashboard de Frutas', style={'font-family': 'Ubuntu'}),
    html.Div(children='''Visualización de la cantidad de diferentes frutas.''', style={'font-family': 'Ubuntu'}),
    dcc.Graph(id='bar-graph', figure=fig),
    dcc.Graph(id='line-graph', figure=fig2),
    dcc.Graph(id='scatter-graph', figure=fig3),
    dcc.Graph(id='pie-chart', figure=fig4)
])

# Correr el servidor
if __name__ == '__main__':
    app.run_server(debug=True, port=8080)