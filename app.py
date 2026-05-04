import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.header('Aplicación para ver resumen de anuncios de carros')
st.write('Proyecto de final de Sprint 7 de Laura Ubaté')

car_data = pd.read_csv('vehicles_us.csv')

# --- Botón 1: Histograma ---
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Histograma para el conjunto de datos de anuncios de venta de carros')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, width='stretch')

# --- Botón 2: Gráfico de dispersión ---
disp_button = st.button('Construir gráfico de dispersión')

if disp_button:
    st.write(
        'Gráfico de dispersión para el conjunto de datos de anuncios de venta de carros')
    fig = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig, width='stretch')

# --- Checkbox: Aprobar gráficos ---
aprobar = st.checkbox('Aprobar gráficos')

if aprobar:
    st.success('¡Gráficos aprobados!')
