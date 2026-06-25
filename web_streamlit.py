'''
Interfaz web utilizando streamlit

Muestra un gráfico de barras con la cantidad de establecimientos
educativos según su ámbito de localización.
"""
'''
import nivel_municipio as nm
import streamlit as st
import programa
import matplotlib.pyplot as plt


def datos() -> list:
    '''
    Obtiene los datos procesados por el módulo programa y los
    transforma en una lista para ser graficado.
    '''
    resultado = programa.controlador()

    urbano, disperso, agrupado, error = resultado

    lista_x = ["Urbano", "Rural Disperso", "Rural Agrupado", "Errores"]
    lista_y = [urbano, disperso, agrupado, error]

    return lista_x, lista_y

def elecciones_modalidades() -> list:
    '''
    dEfinimos las modalidades de las escuelas de la provincia de Bs Aires.
    '''
    lista = programa.apertura_archivo()
    modalidades = []
    for i in lista:
        if i["modalidad"] not in modalidades:
            modalidades.append(i["modalidad"]) 
    return modalidades
        

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

def mapa_mun_niv(Data_set):
    seleccion_mun = st.selectbox("seleccione el municipio", options= nm.nivel_ed)
    if seleccion_mun:
        seleccion_niv = nm.nivel_ed
        niveles_mult = st.multiselect("Selecciona los niveles educativos",options=seleccion_niv, default=seleccion_niv)

        lista_coordenadas = []

        for nivel in niveles_mult:
            2

def barra_niveles() -> None:
    '''
    toma el resultado de la funcion programa.niveles_escuela() y lo grafica en la web mostrando las cantidades
    de escuelas de cada nivel a traves de un grafico de barras
    '''
    

def main() -> None:
    """
    Función principal de la aplicación.
    """
    st.title('Proyecto grupal de Programación 2')
    st.write('¿Cómo es la distribución de las escuelas según su ámbito de localización?')

    x, y = datos()

    fig, ax = plt.subplots(facecolor="#2D2D2F")
    ax.set_facecolor("#2B2B2B")
    bar_container = ax.bar(x, y)
    ax.set(ylabel='Cantidad de escuelas', title='Ámbitos escolares', ylim=(0, 12000))
    ax.bar_label(bar_container, fmt='{:,.0f}')

    st.pyplot(fig)

    mapa()
    barra_niveles()
main()
