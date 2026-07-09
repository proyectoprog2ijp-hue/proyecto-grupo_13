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

def test_contador_ambito():
    '''
    Testeo de la funcion contador_ambito()
    '''
    assert programa.contador_ambito(programa.apertura_archivo("test_datos.csv")) == (["Urbano", "Rural Disperso", "Rural Agrupado", "Errores"],
                                                           [1, 1, 1, 0])
    
def test_elecciones_modalidades():
    '''
    Testeo de la funcion elecciones_modalidades()
    '''
    assert programa.elecciones_modalidades(programa.apertura_archivo("test_datos.csv")) == ["Educación Común", "Educación Técnico Profesional"]