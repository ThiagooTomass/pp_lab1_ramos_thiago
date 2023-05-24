import re
from funciones_interactivas import *


def mostrar_nombre_posicion(lista_jugadores: list):
    '''
    Esta funcion imprime el nombre y posicion de los jugadores del dream team
    recibe la lista y no terona nada
    '''
    for jugador in lista_jugadores:
        print("{0}-{1}".format(jugador["nombre"], jugador["posicion"]))


def mostrar_jugador_segun_indice(lista_jugadores: list, indice: int):
    '''
    Esta funcion muestra las estadisticas segund el indice ingresado por el usuario
    recibe la lista de jugadores y el indice

    '''
    jugador = lista_jugadores[indice]
    for atributo, valor in jugador["estadisticas"].items():
        print("{0} : {1}".format(atributo, valor))

    return jugador


def guardar_dic_segun_indice(lista_jugadores: list, indice: int):
    '''
    Este es el punto 3 todavia no lo hice
    '''
    indice_jugador = mostrar_jugador_segun_indice
    print(indice_jugador)
    guardar_archivo("jugador_elejido.csv", indice_jugador)


def buscar_por_nombre(lista: list, nombre: str):
    '''
    Esta funcion muestra los logros del nombre ingresado por el usuario
    recibe la lista y el nombre a mostras
    '''
    contador = 0
    for lista in lista:
        if re.search(lista["nombre"][0:5], nombre[0:5]) != None:
            print("sus logros son: ")
            for logro in lista["logros"]:
                print("{0}".format(logro))
        else:
            contador += 1
    if (contador == len(lista)):
        print("No se encontro ese jugador")


def promedio_puntos(lista_jugadores: list):
    '''
    Esta funcion muestra el promedio de puntos por partido del dream team
    recibe la lista
    '''
    acumulador = 0
    for jugador in lista_jugadores:
        acumulador += jugador["estadisticas"]["promedio_puntos_por_partido"]
    promedio_puntos_por_partido = acumulador/len(lista_jugadores)
    print("El promedio del Dream Team por partido es: {0}".format(
        promedio_puntos_por_partido))


def ordenar_por_puntos_promedios(lista_original: list):
    '''
    Esta funcion ordena en orden ascendente el promedio de puntos por partido
    recibe la lista 
    retorna la lista completa pero ordenada 
    '''
    lista = lista_original[:]
    lista_derecha = []
    lista_izquierda = []
    if len(lista) <= 1:
        # Devolver solo las alturas
        return lista
    else:
        for jugador in lista[1:]:
            if (jugador["estadisticas"]["promedio_puntos_por_partido"] > lista[0]["estadisticas"]["promedio_puntos_por_partido"]):
                lista_derecha.append(jugador)
            else:
                lista_izquierda.append(jugador)

    lista_izquierda = ordenar_por_puntos_promedios(lista_izquierda)
    lista_derecha = ordenar_por_puntos_promedios(lista_derecha)

    # Incluir el pivot como parte de la lista de alturas
    return lista_izquierda + [lista[0]] + lista_derecha
# Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.


def calcular_max_rebotes(lista: list, key: str):
    '''
    Esta funcion busca y muestra el numero maximo segun su key
    Recibe la lista y la key a evaluar
    '''

    altura_max_inicial = None
    for jugador in lista:
        if (altura_max_inicial is None or jugador["estadisticas"][key] > altura_max_inicial):
            altura_max_inicial = jugador["estadisticas"][key]
            indice_mas_alto = jugador
    print("El jugador con mayor cantidad de {0} es: {1}, sus rebotes son {2}".format(key,
                                                                                     indice_mas_alto["nombre"], indice_mas_alto["estadisticas"][key]))
# Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
# más puntos por partido que ese valor.
