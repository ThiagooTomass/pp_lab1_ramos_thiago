import re
from funciones_interactivas import *


def mostrar_nombre_posicion(lista_jugadores):
    for jugador in lista_jugadores:
        print("{0}-{1}".format(jugador["nombre"], jugador["posicion"]))


def mostrar_jugador_segun_indice(lista_jugadores, indice):
    jugador = lista_jugadores[indice]
    for atributo, valor in jugador["estadisticas"].items():
        print("{0} : {1}".format(atributo, valor))

    return jugador

# Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de la NBA,
# participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.


def guardar_dic_segun_indice(lista_jugadores, indice):
    indice_jugador = mostrar_jugador_segun_indice
    print(indice_jugador)
    guardar_archivo("jugador_elejido.csv", indice_jugador)


def buscar_por_nombre(lista: list, nombre: str):
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
# Calcular y mostrar el promedio de puntos por partido de todo el equipo del
# Dream Team, ordenado por nombre de manera ascendente.


def promedio_puntos(lista_jugadores: list):
    acumulador = 0
    for jugador in lista_jugadores:
        acumulador += jugador["estadisticas"]["promedio_puntos_por_partido"]
    promedio_puntos_por_partido = acumulador/len(lista_jugadores)
    print(promedio_puntos_por_partido)


def ordenar_por_puntos_promedios(lista_original: list):

    lista = lista_original[:]
    lista_derecha = []
    lista_izquierda = []
    if len(lista) <= 1:
        # Devolver solo las alturas
        return lista
    else:
        for numero in lista[1:]:
            if (numero["estadisticas"]["promedio_puntos_por_partido"] > lista[0]["estadisticas"]["promedio_puntos_por_partido"]):
                lista_derecha.append(numero)
            else:
                lista_izquierda.append(numero)

    lista_izquierda = ordenar_por_puntos_promedios(lista_izquierda)
    lista_derecha = ordenar_por_puntos_promedios(lista_derecha)

    # Incluir el pivot como parte de la lista de alturas
    return lista_izquierda + [lista[0]] + lista_derecha
