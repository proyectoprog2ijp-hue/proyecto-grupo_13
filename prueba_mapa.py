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
            lista_latitud.append(float(modalidad["latitud"]))
            lista_longitud.append(float(modalidad["longitud"]))

    print(type(lista_latitud[0]))
    print(lista_latitud[:3])
    print(lista_longitud[:3])

    return lista_nombre, lista_latitud, lista_longitud, contador_comun

mapa_modalidad()
 