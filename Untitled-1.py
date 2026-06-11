import codecs;
import csv
import streamlit as st


def read():
    archivo = open("recorte.csv", newline='')
    lista_datos = list(csv.DictReader(archivo))


    contador_error = 0
    contador_agrupado = 0
    contador_disperso = 0
    contador_urbano = 0

    for categoria in lista_datos:
        if categoria == "urbano":
            contador_urbano += 1
        elif categoria == "rural_disperso":
            contador_disperso += 1
        elif categoria == "rural_agrupado":
            contador_agrupado += 1
        else:
            contador_error += 1
    
    print(lista_datos)


def main():
    read()

main()



