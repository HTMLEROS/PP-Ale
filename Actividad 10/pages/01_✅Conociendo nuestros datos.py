import pandas as pd
import streamlit as st

aeropuertos =  pd.read_csv('ar-airports.csv')
st.title("Parte 1")
st.header("Datos que encontraron")
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

        
