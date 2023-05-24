import re
from funciones_interactivas import *


def mostrar_nombre_posicion(lista_jugadores):
    for jugador in lista_jugadores:
        print("{0}-{1}".format(jugador["nombre"], jugador["posicion"]))


def mostrar_jugador_segun_indice(lista_jugadores, indice):

    for atributo, valor in lista_jugadores[indice]["estadisticas"].items():
        print("{0} : {1}".format(atributo, valor))


# Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de la NBA,
# participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.


def buscar_por_nombre(lista: list, nombre: str):
    lista_nombres = []
    for lista in lista:
        if re.search(lista["nombre"], nombre) != None:
            lista_nombres.append("{0},\n".format(lista))
            nombres = ",".join(lista_nombres)
            print(nombres)
