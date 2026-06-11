import codecs;
import csv
import streamlit as st

def apertura_archivo() -> list:
    '''
    La función comprueba que el archivo dado sea de tipo .csv
    si es así abre el archivo alojado en dirección y retorna
    una lista de diccionarios con los datos del .csv
    de lo contrario retorna una lista vacía
    '''
    direccion = "establecimientos-educativos-12K.csv"

    if direccion[-4:] == ".csv":
        archivo = open(direccion, newline='')
        salida = list(csv.DictReader(archivo))
    else:
        salida = []

    return salida

def contador() -> int int int:
    '''
    
    '''
    datos = apertura_archivo()

    contador_error = 0
    contador_agrupado = 0
    contador_disperso = 0
    contador_urbano = 0

    for categoria in datos:
        if categoria["ambito"] == "Urbano":
            contador_urbano += 1
        elif categoria["ambito"] == "Rural Disperso":
            contador_disperso += 1
        elif categoria["ambito"] == "Rural Agrupado":
            contador_agrupado += 1
        else:
            print(categoria["ambito"])
            contador_error += 1
    
    print(contador_urbano, contador_agrupado,contador_error,contador_disperso)


def main():

    if apertura_archivo() == []:
        print("Archivo inválido")
    else:
        contador()
main()
