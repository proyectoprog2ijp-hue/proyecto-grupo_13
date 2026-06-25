import programa


def nivel_ed(Data_set:list):
    '''
    Filtra los niveles educativos que existen en la provincia
    '''
    niveles = []
    for escuela in Data_set :
        if escuela["nivel"] not in niveles:
            niveles.append(escuela["nivel"]) 
    return niveles

def municipios(Data_set:list):
   '''
   Filtra los municipios de la provincia
   '''
   municipio = []
   for escuela in Data_set :
        if escuela["municipio_nombre"] not in municipio:
            municipio.append(escuela["municipio_nombre"]) 
   return municipio

def mun_niv(Data_set:list):
    '''
    Asocia a las escuelas a sus municipios correspondientes
    agrupandolas por su nivel educativo
    '''
    municipios_nivel = {}  
    for escuela in Data_set:
        municipio = escuela["municipio_nombre"]
        nivel = escuela ["nivel"]
        coord = {
            "latitud": float(escuela["latitud"]),
            "longitud": float(escuela["longitud"])}

        if municipio not in municipios_nivel:
            municipios_nivel[municipio] = {}
        if nivel not in municipios_nivel[municipio] :
            municipios_nivel[municipio][nivel] = [] 
        municipios_nivel[municipio][nivel].append(coord)

    return municipios_nivel
print(mun_niv(programa.apertura_archivo()))  


