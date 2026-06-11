'''
Interfaz web utilizando streamlit

Muestra un gráfico de barras con la cantidad de establecimientos
educativos según su ámbito de localización.
"""
'''
import streamlit as st
import programa

def datos() -> dict:
    '''
    Obtiene los datos procesados por el módulo programa y los
    transforma en un diccionario apto para ser graficado.
    '''
    resultado = programa.controlador()
    
    if resultado == ():
        salida = {}
    else:
        urbano, disperso, agrupado, error = resultado
        salida = {
    "Cant. Urbano": urbano,
    "Cant. Rural Disperso": disperso,
    "Cant. Rural Agrupado": agrupado,
    "Errores de datos": error
    }

    return salida

def main():
    """
    Función principal de la aplicación.

    Muestra el título y la primer pregunta estática desarrollada.
    Luego grafica los resultados obtenidos o informa un error
    si el archivo no posee extensión .csv.
    """

    st.title('Proyecto grupal de Programación 2')
    st.write('¿Cómo es la distribución de las escuelas según su ámbito de localización?')

    resultado = datos()

    if resultado == {}:
        st.error("El archivo no tiene extensión .csv")
    else:
        st.bar_chart(resultado)

main()
