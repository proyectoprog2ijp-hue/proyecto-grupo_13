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

    Ejemplos  :
        datos() -> {"Cant. Urbano": 10261, "Cant. Rural Disperso": 1083, ...}
        datos() -> {"Cant. Urbano": 1, "Cant. Rural Disperso": 0, ...}
        datos() -> {}  (si el archivo no es .csv)
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

def elecciones_modalidades() -> list:
    '''
    dEfinimos las modalidades de las escuelas de la provincia de Bs Aires.
    '''
    return [
        "Educación Artística",
        "Educación Común",
        "Educación Especial",
        "Educación Física",
        "Educación Técnico Profesional",
        "Educación de Jóvenes y Adultos",
        "Psicología Comunitaria y Pedagogía Social"
        ]

def mapa() -> None:
    '''
    Muestra: un menú desplegable para seleccionar una modalidad,
             el total de escuelas de esa modalidad y su ubicación en un
            mapa interactivo.
    '''
    eleccion = st.selectbox("Seleccione Modalidad", options=elecciones_modalidades())
    
    nombre, latitud, longitud, contador = programa.modalidad(eleccion)

    st.metric("Cantidad de escuelas", contador)
    
    dict_coordenadas = {
        "latitude": latitud,
        "longitude": longitud,
    }
    st.map(data=dict_coordenadas, size=50, color="#0044ff", zoom=5)


def main() -> None:
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

    mapa()
main()
