import codecs
import csv
import programa

def test_apertura_archivo():
    '''
    Testeo de la funcion apertura_archivo()
    '''

    assert programa.apertura_archivo("establecimientos-educativos-12K.csv") != []
    assert programa.apertura_archivo("test_datos.csv") != []
    assert programa.apertura_archivo("test_datos.xlsx") == []
    assert programa.apertura_archivo("entrada_datos.txt") == []