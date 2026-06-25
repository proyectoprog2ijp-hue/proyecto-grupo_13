import codecs
import csv
import programa

def archivo_para_testeo():
    '''Usaremos un recorte de todo el archivo csv para poder testear las funciones'''
    direc = "recorte.csv"

    if direc[-4:] == ".csv":
        archivo = open(direc, newline='')
        salida = list(csv.DictReader(archivo))
    else:
        salida = []

    return salida 

def test_contador_ambito():
    '''
    Testeo de la funcion contador_ambito()
    '''
    assert programa.contador_ambito(archivo_para_testeo()) == ( 1, 1, 1, 0)
    assert programa.contador_ambito(()) == ( 0, 0, 0, 0)

#def main():
 #   print(programa.contador_ambito(archivo_para_testeo()))
#main()