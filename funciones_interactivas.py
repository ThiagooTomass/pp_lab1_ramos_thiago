import re


def guardar_archivo(nombre_archivo: str, remplazo: str):
    '''
    Recibe el nombre y extension del archivo a remplazar o crear y el string por el que va a remplazar o crear
    si sale todo bien devuelve true, caso contrario false
    '''
    try:
        with open(nombre_archivo, 'w+') as archivo:
            archivo.write(remplazo)
        return True
    except:
        return False


def busqueda_de_nombres(lista: list, nombre: str):
    lista_segun_nombres = []
    for lista in lista:
        if re.search(lista["nombre"][0:5], nombre[0:5]) != None:
            lista_segun_nombres.append(lista)

    if len(lista_segun_nombres) > 0:
        return lista_segun_nombres
    else:
        print("No existe ese nombre")


def promedio_puntos(lista_jugadores: list, key: str):
    '''
    Esta funcion muestra el promedio de puntos por partido del dream team
    recibe la lista
    '''
    acumulador = 0
    for jugador in lista_jugadores:
        acumulador += jugador["estadisticas"][key]
    promedio = acumulador/len(lista_jugadores)
    return promedio
