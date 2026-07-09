import codecs
import csv

def apertura_archivo(direccion:str="establecimientos-educativos-12K.csv") -> list:
    '''
    La función comprueba que el archivo dado sea de tipo .csv
    si es así abre el archivo alojado en dirección y retorna
    una lista de diccionarios con los datos del .csv
    de lo contrario retorna una lista vacía

    Returns:
        list: lista de diccionarios con los datos del archivo.
        list: lista vacía en caso de error con la extensión.
    
    Ejemplos:
        apertura_archivo() -> [{"establecimiento_nombre": "Esc A", "ambito": "Urbano", ...}, ...]
        apertura_archivo() -> [{"establecimiento_nombre": "Esc B", "ambito": "Rural Disperso", ...}, ...]
        apertura_archivo() -> [] #Si el archivo no tiene extensión .csv
    '''

    if direccion[-4:] == ".csv":
        archivo = open(direccion, newline='')
        salida = list(csv.DictReader(archivo))
    else:
        salida = []

    return salida

def contador_ambito(dataset) -> tuple[list, list]:
    '''
    cuenta los establecimientos según su ámbito y devuelve una tupla.
    
    Retrun:
        tupla: contador_urbano, contador_disperso, contador_agrupado, contador_error
    
    Ejemplos:
        contador_ambito() -> ["Urbano", "Rural Disperso", "Rural Agrupado", "Errores"] [1026, 1083, 654, 2]
        contador_ambito() -> ["Urbano", "Rural Disperso", "Rural Agrupado", "Errores"] [0, 0, 0, 0]  Si no hay dataset
        contador_ambito() -> ["Urbano", "Rural Disperso", "Rural Agrupado", "Errores"] [1, 0, 0, 0]  Si hay solo un Establecimiento Urbano
    '''
    

    contador_error = 0
    contador_agrupado = 0
    contador_disperso = 0
    contador_urbano = 0

    for categoria in dataset:
        if categoria["ambito"] == "Urbano":
            contador_urbano += 1
        elif categoria["ambito"] == "Rural Disperso":
            contador_disperso += 1
        elif categoria["ambito"] == "Rural Agrupado":
            contador_agrupado += 1
        else:
            contador_error += 1
    
    lista_x = ["Urbano", "Rural Disperso", "Rural Agrupado", "Errores"]
    lista_y = [contador_urbano, contador_disperso, contador_agrupado, contador_error]

    return lista_x, lista_y

def elecciones_modalidades(dataset:list) -> list:
    '''
    Definimos las modalidades de las escuelas de la provincia de Bs Aires.
    '''
    modalidades = []
    for i in dataset:
        if i["modalidad"] not in modalidades:
            modalidades.append(i["modalidad"]) 
    return modalidades

def modalidad(modalidad_entrada:str, dataset) -> tuple[list, list, list, int]:
    '''
    Filtra los establecimientos cuya modalidad coincide con
    modalidad_entrada()

    Return:
        lista: nombre de escuelas
        lista: latitudes
        lista: longitudes
        int: contador de escuelas de dicha modalidad
    
    Ejemplos:
        modalidad("Educación Común")     -> (["Esc A", ...], [-34.3, ...], [-60.2, ...], 5)
        modalidad("Educación Artística") -> (["Esc B"], [-37.9], [-61.3], 1)
        modalidad("No existe")           -> ([], [], [], 0)
    '''

    contador_comun = 0
    lista_nombre = []
    lista_latitud = []
    lista_longitud = []

    for modalidad_tabla in dataset:
        if modalidad_tabla["modalidad"] == modalidad_entrada:
            contador_comun += 1
            lista_nombre.append(modalidad_tabla["establecimiento_nombre"])
            lista_latitud.append(float(modalidad_tabla["latitud"]))
            lista_longitud.append(float(modalidad_tabla["longitud"]))

    return lista_nombre, lista_latitud, lista_longitud, contador_comun

def numeros_identificacion(dataset:list) -> list:
    '''
    Filtra todos los números de identificación del archivo y los convierte a una lista.

    Return:
        lista: todos los establecimiento_id
    
    Ejemplos:
        numeros_identificacion() -> ["12345", "67890", "54321", ...]
        numeros_identificacion() -> []  #Si no hay dataset
    '''

    lista_numeros = []
    for escuela in dataset:
        lista_numeros.append(escuela["establecimiento_id"])
    return lista_numeros


def obtener_info_escuela(id_buscado: str, dataset:list) -> dict:
    '''
    Busca una escuela por su establecimiento_id

    Return:
        diccionario: principales datasets del establecimiento seleccionado

    '''
    longitud_dataset = len(dataset)
    i = 0
    seguir = True

    while i <= longitud_dataset and seguir:
        if dataset[i]["establecimiento_id"] == id_buscado:
            escuela = dataset[i]
            informacion = {
                "nombre": escuela["establecimiento_nombre"],
                "nivel": escuela["nivel"],
                "municipio": escuela["municipio_nombre"],
                "direccion": escuela["direccion"],
                "telefono": escuela["telefono"],
                "mail": escuela["email"],
                "turnos": escuela["turnos"],
                "LAT": escuela["latitud"],
                "LON": escuela["longitud"],
                "categoria": escuela["categoria"],
                "desfavorabilidad": escuela["desfavorabilidad"]
            }
            seguir = False
        i += 1
    return informacion

def nivel_ed(Data_set:list) -> list:
    '''
    Filtra los niveles educativos que existen en la provinciadef contador_niv(Data_set:list)->tuple[list,list]:
    lista_niveles = nivel_ed(Data_set)
    lista_salida = []    
    for nivel in lista_niveles:
        contador = 0
        for fila in Data_set :
            if fila["nivel"] == nivel:
                contador += 1
        lista_salida.append[contador]
    return lista_niveles, lista_salida
    

    return:
        lista : lista con los todos los niveles educativo que existen en la provincia de BSAS
    '''
    niveles = []
    for escuela in Data_set :
        if escuela["nivel"] not in niveles:
            niveles.append(escuela["nivel"]) 
    return niveles

def municipios(Data_set:list):
   '''
   Filtra los municipios de la provincia

   return:
        lista: lista con todos los municipios de la provincia de BSAS
   '''
   municipio = []
   for escuela in Data_set :
        if escuela["municipio_nombre"] not in municipio:
            municipio.append(escuela["municipio_nombre"]) 
   return municipio

def mun_niv(Data_set:list)->dict:
    '''
    Asocia a las escuelas a sus municipios correspondientes
    agrupandolas por su nivel educativo

    return:
        
        dict: diccionario de cada municipio con las coordenadas y niveles educativos 
              de las escuelas asociadas a el
    '''
    municipios_nivel = {}  
    for escuela in Data_set:
        municipio = escuela["municipio_nombre"]
        nivel = escuela ["nivel"]
        coord = {
            "LAT": float(escuela["latitud"]),
            "LON": float(escuela["longitud"])}

        if municipio not in municipios_nivel:
            municipios_nivel[municipio] = {}
        if nivel not in municipios_nivel[municipio] :
            municipios_nivel[municipio][nivel] = [] 
        municipios_nivel[municipio][nivel].append(coord)

    return municipios_nivel


def contador_niv(Data_set:list)->tuple[list,list]:
    '''
    Dado un data set, crea dos listas con los tipos de niveles educativos 
    y la cantidad de cada uno.

    return:
        tuple : retorna una tupla con dos listas, una que contiene los distintos niveles educativos
               y la otra contiene la cantidad de niveles educactivos, cada lista ordenada de igual manera.
    '''
    lista_niveles = nivel_ed(Data_set)
    lista_salida = []    
    for nivel in lista_niveles:
        contador = 0
        for fila in Data_set :
            if fila["nivel"] == nivel:
                contador += 1
        lista_salida.append(contador)
    return lista_niveles, lista_salida

def dependencias(data_set:list) -> dict:
    '''
    Devuelve un diccionario con los porcentajes de cada tipo de dependencia de las escuelas en la provincia.
    Primero analiza el dataset y luego genera un diccionario con el tipo de dependencia y el porcentaje de escuelas que pertenecen a esa dependencia.
    Las claves del diccionario será el tipo de dependencia y el valor será el porcentaje de escuelas que pertenecen a esa dependencia.
    
    return:
        dict: diccionario con los porcentajes de cada tipo de dependencia de las escuelas en la provincia.
              value: dependencia, key: porcentaje de escuelas que pertenecen a esa dependencia.
    '''
    salida = {}
    total_escuelas = len(data_set)

    for escuela in data_set:
        dependencia = escuela["dependencia"]
        if dependencia not in salida:
            salida[dependencia] = 0
        salida[dependencia] += 1

    for dependencia in salida:
        salida[dependencia] = (salida[dependencia] / total_escuelas) * 100

    return salida