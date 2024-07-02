import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('/Users/sebastianramirezselame/Desktop/proyecto5-1/vehicles_us.csv')
st.header('Análisis de Anuncios de Venta de Coches')

if st.button('Construir Histograma'):
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig)

if st.button('Construir Gráfico de Dispersión'):
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig)
