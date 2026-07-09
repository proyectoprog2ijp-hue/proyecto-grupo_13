import programa
def dataset():
    return programa.apertura_archivo("test_datos.csv")

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
    
def test_elecciones_modalidades():
    """
    Testeo de la función elecciones_modalidades()
    """
    assert programa.elecciones_modalidades(dataset()) == [
        "Educación Común",
        "Educación Técnico Profesional"
    ]

def test_contador_ambito():
    """
    Testeo de la función contador_ambito()
    """
    assert programa.contador_ambito(dataset()) == (
        ["Urbano", "Rural Disperso", "Rural Agrupado", "Errores"],
        [1, 1, 1, 0]
    )

def test_numeros_identificacion():
    """
    Testeo de la función numeros_identificacion()
    """
    assert programa.numeros_identificacion(dataset()) == [
        "24087",
        "24681",
        "203"
    ]

def test_municipios():
    """
    Testeo de la función municipios()
    """
    assert programa.municipios(dataset()) == [
        "Salto",
        "Zárate",
        "La Plata"
    ]

def test_contador_niv():
    """
    Testeo de la función contador_niv()
    """
    assert programa.contador_niv(dataset()) == (
        ["Nivel Secundario", "Nivel Inicial"],
        [2, 1]
    )

def test_cantidad_modalidades():
    modalidades = programa.elecciones_modalidades(dataset())
    assert len(modalidades) == 2