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

    seleccion_mun = st.selectbox("seleccione el municipio", options= nm.municipios(Data_set))
    if seleccion_mun:
        seleccion_niv = nm.nivel_ed(Data_set)
        niveles_mult = st.multiselect("Selecciona los niveles educativos",options=seleccion_niv, default=seleccion_niv)

        lista_coordenadas = []

        for nivel in niveles_mult:
            if nivel in nm.mun_niv(Data_set)[seleccion_mun]:
                lista_coordenadas += nm.mun_niv(Data_set)[seleccion_mun][nivel]
        if lista_coordenadas:
            st.map(data=lista_coordenadas)

def grafico_barra_niveles(dataset:list) -> None:
    '''
    toma el resultado de la funcion programa.niveles_escuela(dataset) y lo grafica en la web mostrando las cantidades
    de escuelas de cada nivel a traves de un grafico de barras
    '''
    st.header("Cantidad de escuelas según su nivel educativo")

    fig, ax = plt.subplots(facecolor="#59FF00FF")

    niveles = ["Ciclo de Iniciación", "Nivel Inicial", "Nivel Primario", "Nivel Secundario", "Formación Integral", "Nivel Superior", "Plan Fines (Trayectos y Deudores)", "Educación Física (C.E.F.)", "Formación Profesional", "Ciclo Medio", "Psicología Comunitaria y Pedagogía Social (C.E.C)", "Cursos y Talleres", "Residencia Laboral,Pasantías, Artística"]
    cantidad = programa.niveles_escuela(dataset)
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
    seleccion = st.selectbox("Seleccione o escriba el número de identificación", options=programa.numeros_identificacion(dataset))

    if seleccion:
        informacion = programa.obtener_info_escuela(seleccion, dataset)

        dict_coordenadas = {
            "lat": [float(informacion["LAT"])],
            "lon": [float(informacion["LON"])]
        }

        tarjeta = st.container(border=True)
        tarjeta.write("Nombre: " + informacion["nombre"])
        tarjeta.write("• Nivel: " + informacion["nivel"])
        tarjeta.write("• Municipio: " + informacion["municipio"])
        tarjeta.write("• Dirección: " + informacion["direccion"])
        tarjeta.write("• Teléfono: " + informacion["telefono"])
        tarjeta.write("• Mail: " + informacion["mail"])
        tarjeta.write("• Turnos: " + informacion["turnos"])
        tarjeta.write("")
        tarjeta.map(data=dict_coordenadas, size=50, color="#00e1ff", zoom=14)

def main() -> None:
    """
    Función principal de la aplicación.
    """
    st.title('Proyecto grupal de Programación 2')

    dataset = programa.apertura_archivo()

    grafico_barra_ambito(dataset)
    grafico_barra_niveles(dataset)

    mapa_modalidad(dataset)
    mapa_mun_niv(dataset)

    informacion_escuela(dataset)
main()
