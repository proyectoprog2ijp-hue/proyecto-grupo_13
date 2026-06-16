import codecs
import csv
import programa 


def mapa_modalidad(modalidad_entrada):
    datos = programa.apertura_archivo()

    contador_comun = 0
    lista_nombre = []
    lista_latitud = []
    lista_longitud = []

    for modalidad_tabla in datos:
        if modalidad_tabla["modalidad"] == modalidad_entrada:
            contador_comun += 1
            lista_nombre.append(modalidad_tabla["establecimiento_nombre"])
            lista_latitud.append(float(modalidad_tabla["latitud"]))
            lista_longitud.append(float(modalidad_tabla["longitud"]))

    return lista_nombre, lista_latitud, lista_longitud, contador_comun 