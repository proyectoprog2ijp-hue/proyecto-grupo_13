'''
Interfaz web utilizando streamlit

Muestra un gráfico de barras con la cantidad de establecimientos
educativos según su ámbito de localización.
"""
'''
import streamlit as st
import programa
import matplotlib.pyplot as plt

def grafico_barra_ambito(dataset:list) -> None:
    '''
    La funcion muestra un grafico de barras utilizando libreria matplotlib acerca de la cantidad
    de escuelas según cada ámbito, contemplando si hay errores
    '''
    st.header("Cantidad de escuelas según su ámbito")
    st.write('¿Cómo es la distribución de las escuelas según su ámbito de localización?')

    x, y = programa.contador_ambito(dataset)

    fig, ax = plt.subplots(facecolor="#2D2D2F")
    ax.set_facecolor("#2B2B2B")
    bar_container = ax.bar(x, y)
    ax.set(ylabel='Cantidad de escuelas', title='Ámbitos escolares', ylim=(0, 12000))
    ax.bar_label(bar_container, fmt='{:,.0f}')

    st.pyplot(fig)        

def mapa_modalidad(dataset:list) -> None:
    '''
    Muestra: un menú desplegable para seleccionar una modalidad,
             el total de escuelas de esa modalidad y su ubicación en un
            mapa interactivo.
    '''
    st.header("Ubicación escuelas según su modalidad")
    st.write("¿Cuáles y cuántos son los establecimientos que hay en una X localidad?")

    eleccion = st.selectbox("Seleccione Modalidad", options=programa.elecciones_modalidades(dataset))
    
    nombre, latitud, longitud, contador = programa.modalidad(eleccion, dataset)

    st.metric("Cantidad de escuelas", contador)
    
    dict_coordenadas = {
        "LAT": latitud,
        "LON": longitud,
    }
    st.map(data=dict_coordenadas, size=50, color="#0044ff", zoom=5)

def mapa_mun_niv(Data_set):
    st.header("Ubicación escuelas según el municipio y su nivel")
    st.write("¿Cuáles son los establecimientos de nivel X en el municipio Y ?")
    datos = programa.mun_niv(Data_set)
    seleccion_mun = st.selectbox("seleccione el municipio", options= programa.municipios(Data_set))
    if seleccion_mun:
        seleccion_niv = programa.nivel_ed(Data_set)
        niveles_mult = st.multiselect("Selecciona los niveles educativos",options=seleccion_niv, default=seleccion_niv)
        
        lista_coordenadas = []

        for nivel in niveles_mult:
            if nivel in datos[seleccion_mun]:
                lista_coordenadas += datos[seleccion_mun][nivel]
        if lista_coordenadas:
            st.map(data=lista_coordenadas)

def grafico_barra_niveles(dataset:list) -> None:
    '''
    toma el resultado de la funcion programa.niveles_escuela(dataset) y lo grafica en la web mostrando las cantidades
    de escuelas de cada nivel a traves de un grafico de barras
    '''
    st.header("Cantidad de escuelas según su nivel educativo")
    st.write("¿Cuál es la cantidad de escuelas de cada nivel que hay en la provincia de Buenas Aires?")

    fig, ax = plt.subplots(facecolor="#59FF00FF")
    niveles , cantidad = programa.contador_niv(dataset)
    error = [0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

    ax.barh(niveles, cantidad, xerr=error, align="center")
    ax.yaxis.set_inverted(True)
    ax.set_xlabel("Cantidad de escuelas.")
    ax.set_title("Cantidad de escuelas por nivel educativo.")
    
    st.pyplot(fig)

def informacion_escuela(dataset:list) -> None:
    '''
    Muestra un menú desplegable para seleccionar el numero de identificación de la escuela y luego muestra la información de esa escuela y la ubicación en un mapa.
    '''
    st.header("Información de la escuela")
    st.write("¿Cuál es la categoría y el nivel de desfavorabilidad de una institución educativa X?")
    seleccion = st.selectbox("Seleccione o escriba el número de identificación", options=programa.numeros_identificacion(dataset))

    if seleccion:
        informacion = programa.obtener_info_escuela(seleccion, dataset)

        dict_coordenadas = {
            "lat": [float(informacion["LAT"])],
            "lon": [float(informacion["LON"])]
        }

        tarjeta = st.container(border=True)
        tarjeta.subheader(informacion["nombre"])
        tarjeta.markdown(":green-badge[Categoria: " + informacion["categoria"] + "]"
                         ":orange-badge[Desfavorabilidad: " + informacion["desfavorabilidad"] + "]")
        tarjeta.write("• Nivel: " + informacion["nivel"])
        tarjeta.write("• Municipio: " + informacion["municipio"])
        tarjeta.write("• Dirección: " + informacion["direccion"])
        tarjeta.write("• Teléfono: " + informacion["telefono"])
        tarjeta.write("• Mail: " + informacion["mail"])
        tarjeta.write("• Turnos: " + informacion["turnos"])
        tarjeta.write("")
        tarjeta.map(data=dict_coordenadas, size=50, color="#00e1ff", zoom=14)

def grafico_dependencias(dataset:list) -> None:
    '''
    Muestra un gráfico circular generado por matplotlib según los porcentajes de escuelas que hay en la provincia según su dependencia.
    '''
    st.header("Porcentaje de escuelas según su dependencia")
    st.write("¿Cuál es el porcentaje de escuelas según su dependencia en la provincia de Buenos Aires?")

    dependencias = programa.dependencias(dataset)
    tipo_dependencia = list(dependencias.keys())
    cantidades = list(dependencias.values())

    fig, ax = plt.subplots()
    ax.pie(cantidades,
           labels=tipo_dependencia,
           autopct='%1.1f%%')
    ax.axis('equal')

    st.pyplot(fig)

def main() -> None:
    """
    Función principal de la aplicación.
    """
    st.set_page_config(
    page_title="Grupo 13 — Prog II",
    page_icon="🏫")

    st.title("Análisis de establecimientos educativos en la provincia de Buenos Aires")
    st.header("Grupo 13 — Programación II")
    st.image("logo_pagina.png")

    dataset = programa.apertura_archivo()
    seleccion = st.radio(
        "Seleccioná una opción para comenzar:", 
        options=[
            "Gráfico de barras por ámbito",
            "Gráfico de barras por nivel educativo",
            "Mapa de escuelas según modalidad", 
            "Mapa de escuelas según municipio y nivel educativo",
            "Información de una escuela",
            "Gráfico según el porcentaje de dependencias"],
        index=None)

    if dataset == []:
        st.error("El archivo no tiene extensión .csv")
    elif seleccion == "Gráfico de barras por ámbito":
        grafico_barra_ambito(dataset)
    elif seleccion == "Gráfico de barras por nivel educativo":
        grafico_barra_niveles(dataset)
    elif seleccion == "Mapa de escuelas según modalidad":
        mapa_modalidad(dataset)
    elif seleccion == "Mapa de escuelas según municipio y nivel educativo":
        mapa_mun_niv(dataset)
    elif seleccion == "Información de una escuela":
        informacion_escuela(dataset)
    elif seleccion == "Gráfico según el porcentaje de dependencias":
        grafico_dependencias(dataset)
    else:
        st.info("Seleccione una opción para continuar")
main()
