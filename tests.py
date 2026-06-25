import programa

def test_apertura_archivo():
    '''
    Testeo de la funcion apertura_archivo()
    '''
    #la extensión del archivo es correcta
    assert programa.apertura_archivo("establecimientos-educativos-12K.csv") != []
    assert programa.apertura_archivo("test_datos.csv") != []
    #la extensión del archivo es incorrecta
    assert programa.apertura_archivo("test_datos.xlsx") == []
    assert programa.apertura_archivo("entrada_datos.txt") == []