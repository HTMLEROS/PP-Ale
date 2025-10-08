import pandas as pd
import streamlit as st

aeropuertos =  pd.read_csv('ar-airports.csv')
st.title("Parte 1")
st.header("Datos que encontraron")
st.write("Este Dataset (ar-airports.csv) contiene información sobre todos los puertos, aeropuertos, helipuertos y bases de despegue de globos aeroestáticos de la república.")
st.write("**Parte 1:** trabajaremos con el tamaño del dataset en tablas y columnas, los nombres de los aeropuertos que aparecen y de que tamaño son.")
st.write("POdemos observar que existen 6 tipos de aeropuertos: Grandes, Medianos, Chicos, Helipuertos, Ballonports y Cerrados. Tambien, observamos que sus columnas estan organizadas por ID, Nombre del aeropuerto, Ubicación entre otros datos relevantes.")
filas, columnas = aeropuertos.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = aeropuertos.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')
    
    
nombres = aeropuertos['name'].unique()
tipos = aeropuertos['type'].unique()
ntipos = len(aeropuertos['type'].unique())

with st.expander("¿Cuáles son los nombres de los Aeropuertos? **NAME**"):
    st.write(nombres)
with st.expander("¿Cuántos son los valores únicos de la columna **TYPE**?"):
    st.write(tipos)
with st.expander("¿Cuáles son los valores únicos de la columna **TYPE**?"):
    st.write(ntipos)
with st.expander("¿Cuáles son los nombres de las columnas ?"):
   
    st.write(aeropuertos.columns)

        
