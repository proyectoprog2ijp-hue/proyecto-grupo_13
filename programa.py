import codecs
import csv

def apertura_archivo() -> list:
    '''
    La función comprueba que el archivo dado sea de tipo .csv
    si es así abre el archivo alojado en dirección y retorna
    una lista de diccionarios con los datos del .csv
    de lo contrario retorna una lista vacía

    Returns:
        list: lista de diccionarios con los datos del archivo.
        list: lista vacía en caso de error con la extensión.
    '''
    direccion = "establecimientos-educativos-12K.csv"

    if direccion[-4:] == ".csv":
        archivo = open(direccion, newline='')
        salida = list(csv.DictReader(archivo))
    else:
        salida = []

    return salida

def contador() -> tuple[int, int, int, int]:
    '''
    cuenta los establecimientos según su ámbito y devuelve una tupla.
    
    Retrun:
        tupla: contador_urbano, contador_disperso, contador_agrupado, contador_error
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
            contador_error += 1
    
    return contador_urbano, contador_disperso, contador_agrupado, contador_error

def controlador() -> tuple:
    """
    Coordina la ejecución del programa.

    Verifica si el archivo pudo abrirse correctamente.
    En ese caso, realiza el conteo de establecimientos.

    Returns:
        tupla: Resultado de la función contador().
        tupla: vacía, en caso de extensión incorrecta.
    """
    if apertura_archivo() == []:
        salida = ()
    else:
        salida = contador()
    
    return salida
