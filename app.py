import pandas as pd
import plotly.express as px
import streamlit as st


st.header('Aplicación Vehículos Usados')  

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir Histograma') # crear un botón
graph_button = st.button('Construir Gráfico de Dispersión')

        
if hist_button: # al hacer click en el botón
    # escribir un mensaje
    st.write('Creación de un Histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig1 = px.histogram(car_data, x="odometer")
        
    #mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)




if graph_button: # al hacer click in el botón
    st.write('Construir un Gráfico de dispersión para la columna odómetro')
    
    fig2 = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig2, use_container_width=True)
