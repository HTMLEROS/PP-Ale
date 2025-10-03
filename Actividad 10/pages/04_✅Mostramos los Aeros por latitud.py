import streamlit as st
import pandas as pd

# Cargar datos
aeros = pd.read_csv("ar-airports.csv")

st.title("Filtro con **Slider**")

st.write("Podés mover el slider para seleccionar un rango de latitudes y ver qué aeropuertos entran en ese rango.")

# Obtener valores mínimos y máximos de latitud
min_lat = float(aeros['latitude_deg'].min())
max_lat = float(aeros['latitude_deg'].max())

# Slider para rango de latitudes
lat_range = st.slider(
    "Seleccioná el rango (latitud)",
    min_value=min_lat,
    max_value=max_lat,
    value=(min_lat, max_lat)
)

# Filtrar por latitud
filtrados = aeros[(aeros['latitude_deg'] >= lat_range[0]) & (aeros['latitude_deg'] <= lat_range[1])]

st.subheader(f"Aeropuertos en el rango {lat_range[0]:.2f} a {lat_range[1]:.2f}")
st.write(f"Se encontraron {len(filtrados)} aeropuertos.")
st.dataframe(filtrados[['name', 'municipality', 'latitude_deg', 'longitude_deg']])

