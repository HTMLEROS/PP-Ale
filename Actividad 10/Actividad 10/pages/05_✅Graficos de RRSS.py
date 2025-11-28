import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Gráficos de Redes Sociales")
st.write("En esta sección, podrás analizar el uso de redes sociales según la edad y las horas de uso.")

# Cargar datos
df = pd.read_csv("usos-digitales.csv")

# --- Barra lateral de filtros ---
st.sidebar.header("Filtros")

# Red
red_social_seleccionada = st.sidebar.selectbox(
    "Seleccioná una red social:",
    options=['instagram', 'tiktok', 'youtube', 'twiter'],
    format_func=lambda x: x.capitalize()
)

# Filtro edad
edades = sorted(df['Edad'].unique())
edad_seleccionada = st.sidebar.slider(
    "Seleccioná un rango de edad:",
    min_value=int(df['Edad'].min()),
    max_value=int(df['Edad'].max()),
    value=(int(df['Edad'].min()), int(df['Edad'].max()))
)

# Filtrar x horas de uso
horas_opciones = df[red_social_seleccionada].unique().tolist()
horas_seleccionadas = st.sidebar.multiselect(
    f"Seleccioná las horas de uso para {red_social_seleccionada.capitalize()}:",
    options=horas_opciones,
    default=horas_opciones
)

# --- Filtrado de datos ---
df_filtrado = df[
    (df['Edad'] >= edad_seleccionada[0]) &
    (df['Edad'] <= edad_seleccionada[1]) &
    (df[red_social_seleccionada].isin(horas_seleccionadas))
]

st.subheader(f"Análisis para: {red_social_seleccionada.capitalize()}")

if df_filtrado.empty:
    st.warning("No hay datos que coincidan con los filtros seleccionados.")
else:
    #Carga
    tipo_grafico = st.radio(
        "Elegí el tipo de gráfico:",
        ("Barras", "Torta"),
        key='tipo_grafico'
    )

    # Agrupar x red seleccionada (horas de uso)
    conteo_horas = df_filtrado[red_social_seleccionada].value_counts().reset_index()
    conteo_horas.columns = ['Horas de Uso', 'Cantidad de Usuarios']

    if tipo_grafico == "Barras":
        fig = px.bar(
            conteo_horas,
            x='Horas de Uso',
            y='Cantidad de Usuarios',
            color='Horas de Uso',
            title=f'Distribución de horas de uso para {red_social_seleccionada.capitalize()}',
            labels={'Cantidad de Usuarios': 'Cantidad de Usuarios', 'Horas de Uso': 'Horas de Uso'}
        )
    else: # Torta
        fig = px.pie(
            conteo_horas,
            names='Horas de Uso',
            values='Cantidad de Usuarios',
            title=f'Proporción de horas de uso para {red_social_seleccionada.capitalize()}',
            hole=0.3
        )
        fig.update_traces(
            pull=[0.05] * len(conteo_horas),
            textinfo='percent+label'
        )

    st.plotly_chart(fig, use_container_width=True)

    # Tabla expandible
    with st.expander("Ver datos filtrados"):
        st.dataframe(df_filtrado[['Edad', 'Género', red_social_seleccionada]])
