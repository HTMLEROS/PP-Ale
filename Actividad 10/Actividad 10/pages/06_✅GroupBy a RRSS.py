import streamlit as st
import pandas as pd
import matplotlib.pyplot as pl

st.set_page_config(layout="wide")

st.title("GroupBy en Redes Sociales")
st.write("En esta sección, agrupamos por mes y por año las entradas del Dataset.")

df = pd.read_csv("usos-digitales.csv")

#formato
df["Marca temporal"] = pd.to_datetime(df["Marca temporal"])

#Agrupaciones
agrupado_por_mes = df.groupby(df["Marca temporal"].dt.to_period("M")).size()
agrupado_por_año = df.groupby(df["Marca temporal"].dt.to_period("Y")).size()

#Gráfico de barras
st.subheader("Entradas por mes")

fig1 = pl.figure(figsize=(10, 5))
pl.bar(agrupado_por_mes.index.astype(str), agrupado_por_mes.values)
pl.xticks(rotation=45)
pl.title("Entradas por mes")
pl.xlabel("Mes")
pl.ylabel("Cantidad de entradas")
pl.tight_layout()

st.pyplot(fig1)


#Gráfico de torta
st.subheader("Entradas por año")

fig2 = pl.figure(figsize=(7, 7))
pl.pie(
    agrupado_por_año.values,
    labels=agrupado_por_año.index.astype(str),
    autopct="%1.1f%%"
)
pl.title("Entradas por año")
pl.tight_layout()

st.pyplot(fig2)

