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
    
    Ejemplos:
        apertura_archivo() -> [{"establecimiento_nombre": "Esc A", "ambito": "Urbano", ...}, ...]
        apertura_archivo() -> [{"establecimiento_nombre": "Esc B", "ambito": "Rural Disperso", ...}, ...]
        apertura_archivo() -> [] #Si el archivo no tiene extensión .csv
    '''
    direccion = "establecimientos-educativos-12K.csv"

    if direccion[-4:] == ".csv":
        archivo = open(direccion, newline='')
        salida = list(csv.DictReader(archivo))
    else:
        salida = []

    return salida

def contador_ambito() -> tuple[int, int, int, int]:
    '''
    cuenta los establecimientos según su ámbito y devuelve una tupla.
    
    Retrun:
        tupla: contador_urbano, contador_disperso, contador_agrupado, contador_error
    
    Ejemplos:
        contador_ambito() -> (1026, 1083, 654, 2)
        contador_ambito() -> (0, 0, 0, 0)  Si no hay datos
        contador_ambito() -> (1, 0, 0, 0)  Si hay solo un Establecimiento Urbano
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

def modalidad(modalidad_entrada:str) -> tuple[list, list, list, int]:
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
    datos = apertura_archivo()

    contador_comun = 0
    lista_nombre = []
    lista_latitud = []
    lista_longitud = []

    for modalidad_tabla in datos:
        if modalidad_tabla["modalidad"] == modalidad_entrada:
            contador_comun += 1
            lista_nombre.append(modalidad_tabla["establecimiento_nombre"])
            lista_latitud.append(float(modalidad_tabla["latitud"]))
            lista_longitud.append(float(modalidad_tabla["longitud"]))

    return lista_nombre, lista_latitud, lista_longitud, contador_comun

def controlador() -> tuple:
    """
    Coordina la ejecución del programa.

    Verifica si el archivo pudo abrirse correctamente.
    En ese caso, realiza el conteo de establecimientos.

    Returns:
        tupla: Resultado de la función contador().
        tupla: vacía, en caso de extensión incorrecta.
    
    Ejemplos:
        controlador() -> (10261, 1083, 654, 2)
        controlador() -> (1, 0, 0, 0)  #Si solo hay un establecimiento urbano)
        controlador() -> ()            #Si el archivo no es .csv)
    """
    if apertura_archivo() == []:
        salida = ()
    else:
        salida = contador_ambito()
    
    return salida

def niveles_escuela() -> tuple:
    '''
    filtra los niveles de escuela y retorna una tupla con la cantidad de
    escuelas de cada nivel, en el siguiente orden:
    niveles_escuela() -> (ciclo_iniciacion, inicial, primario, secundario, for_integral, superior, plan_fines, ed_fisica, 
                         for_profesional, casos_extras, ciclo_medio, psico_comun_pedagogia_social, cursos_talleres,
                        residencia_laboral_pasantias_artistica)
    ejemplos:
    niveles_escuela() -> (1200, 800, 10000) Si hay 1200 escuelas de nvl. inicial, 800 de nvl. primario y 10000 nvl. secundario
    niveles_escuela() -> (0, 0, 0) Si no hay escuelas de ningun nivel
    niveles_escuela() -> (23, 0, 0)Si solo hay 23 escuelas de nivel inicial
    '''
    datos = apertura_archivo()
    ciclo_iniciacion = 0
    inicial = 0
    primario = 0
    secundario = 0
    for_integral = 0
    superior = 0
    plan_fines = 0
    ed_fisica = 0
    for_profesional = 0
    ciclo_medio = 0
    psico_comun_pedagogia_social = 0
    cursos_talleres = 0
    residencia_laboral_pasantias_artistica = 0
    for nivel in datos:
        if nivel["nivel"] == "Ciclo de Iniciación":
            ciclo_iniciacion += 1
        elif nivel["nivel"] == "Nivel Inicial":
            inicial += 1
        elif nivel["nivel"] == "Nivel Primario":
            primario += 1
        elif nivel["nivel"] == "Nivel Secundario":
            secundario += 1
        elif nivel["nivel"] == "Formación Integral":
            for_integral += 1
        elif nivel["nivel"] == "Nivel Superior":
            superior += 1
        elif nivel["nivel"] == "Plan Fines (Trayectos y Deudores)":
            plan_fines += 1
        elif nivel["nivel"] == "Educación Física (C.E.F.)":
            ed_fisica += 1
        elif nivel["nivel"] == "Formación Profesional":
            for_profesional += 1
        elif nivel["nivel"] == "Ciclo Medio":
            ciclo_medio += 1
        elif nivel["nivel"] == "Psicología Comunitaria y Pedagogía Social (C.E.C)":
            psico_comun_pedagogia_social += 1
        elif nivel["nivel"] == "Cursos y Talleres":
            cursos_talleres += 1
        else:
            residencia_laboral_pasantias_artistica += 1
    return ciclo_iniciacion, inicial, primario, secundario, for_integral, superior, plan_fines, ed_fisica, for_profesional, ciclo_medio, psico_comun_pedagogia_social, cursos_talleres, residencia_laboral_pasantias_artistica

