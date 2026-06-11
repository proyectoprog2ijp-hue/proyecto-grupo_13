import streamlit as st
import programa

def datos():
    contador = programa.controlador()

    urbano, disperso, agrupado, error = contador

    return {
    "Cantidad Urbano": urbano,
    "Cantidad Rural Disperso": disperso,
    "Cantidad Rural Agrupado": agrupado,
    "Errores de datos": error
    }

def streamlit():
    st.title ('Proyecto grupal de Programación 2')
    st.write ('¿Cómo es la distribución de las escuelas según su ámbito de localización? ')
    st.bar_chart(datos())
