import codecs
import csv
import programa 


def mapa_modalidad():
    datos = programa.apertura_archivo()

    contador_comun = 0
    lista_nombre = []
    lista_latitud = []
    lista_longitud = []

    for modalidad in datos:
        if modalidad["modalidad"] == "Educación Común":
            contador_comun += 1
            lista_nombre.append(modalidad["establecimiento_nombre"])
            lista_latitud.append(modalidad["latitud"])
            lista_longitud.append(modalidad["longitud"])
    return lista_nombre, lista_latitud, lista_longitud, contador_comun
 