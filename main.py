import codecs;
import csv
import streamlit as st

archivo = open("establecimientos-educativos-12K.csv", newline='')
leectura_archivo = csv.DictReader(archivo)

def read():
    for categoria in leectura_archivo:
        return(categoria['establecimiento_nombre'])


def main():
    read()

main()
