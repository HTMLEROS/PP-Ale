import streamlit as st
import pandas as pd
import plotly.express as px

aeros = pd.read_csv('ar-airports.csv')

st.title("Gráfico interactivo")
st.write("En esta sección podrás usar el switch para elegir entre un gráfico de barras o uno de torta donde se graficará la **concentración de aeropuertos por provincia**.")

# Selector de tipo de gráfico
tipo_grafico = st.radio(
    "Elegí el tipo de gráfico:",
    ("Barras", "Torta")
)

conteo_tipos = aeros['region_name'].value_counts().reset_index()
conteo_tipos.columns = ['Provincia', 'Cantidad']

if tipo_grafico == "Barras":
    fig = px.bar(
        conteo_tipos,
        x='Provincia',
        y='Cantidad',
        color='Provincia',
        title='Cantidad de Aeropuertos por Provincia',
        labels={'Cantidad': 'Cantidad de Aeropuertos', 'Provincia': 'Provincia'}
    )
else:
    fig = px.pie(
        conteo_tipos,
        names='Provincia',
        values='Cantidad',
        title='Distribución de Aeropuertos por Provincia',
        hole=0, # Vi en google que se pone para que no quede agujero en el centro
    )

    # Efecto del clcik
    fig.update_traces(
        pull=[0.1]*len(conteo_tipos),  # (?
        hoverinfo='label+percent',
        textinfo='percent+label'
    )

# Si no funciona lo reinicias y rezás
st.plotly_chart(fig, use_container_width=True)


