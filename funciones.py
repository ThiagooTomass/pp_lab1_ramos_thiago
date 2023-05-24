
from funciones_interactivas import *

# EJERCICIO 1


def mostrar_nombre_posicion(lista_jugadores: list):
    '''
    Esta funcion imprime el nombre y posicion de los jugadores del dream team
    recibe la lista y no terona nada
    '''

    for jugador in lista_jugadores:
        print("{0}-{1}".format(jugador["nombre"], jugador["posicion"]))

# EJERCICIO 2


def mostrar_jugador_segun_indice(lista_jugadores: list, indice: int):
    '''
    Esta funcion muestra las estadisticas segund el indice ingresado por el usuario
    recibe la lista de jugadores y el indice

    '''

    for atributo, valor in lista_jugadores[indice]["estadisticas"].items():
        print("{0} : {1}".format(atributo, valor))

    return lista_jugadores[indice]

# EJERCICIO 3


def guardar_dic_segun_indice(lista_jugadores: list, indice: int):
    '''
    Este es el punto 3 todavia no lo hice
    '''
    indice_jugador = mostrar_jugador_segun_indice
    print(indice_jugador)
    guardar_archivo("jugador_elejido.csv", indice_jugador)

# EJERCICIO 4


def buscar_por_nombre(lista_jugadores: list, nombre: str):
    '''
    Esta funcion muestra los logros del nombre ingresado por el usuario
    recibe la lista y el nombre a mostras
    '''
    lista_jugador = busqueda_de_nombres(lista_jugadores, nombre)

    try:
        for jugador in lista_jugador:
            print("\n---{0}---\n".format(jugador["nombre"]))
            for logros in jugador["logros"]:
                print(logros)
    except:
        pass


# EJERCICIO 5


def ordenar_por_puntos_promedios(lista_jugadores: list):
    '''
    Esta funcion ordena en orden ascendente el promedio de puntos por partido
    recibe la lista 
    retorna la lista completa pero ordenada 
    '''

    lista = lista_jugadores[:]
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


# EJERCICIO 6


def salon_de_la_fama(lista_jugadores: list, nombre: str):
    '''
    Esta funcion pregunta si el nombre ingresado tiene por lo menos 5 coincidencias con el nombre, al princio.
    si es asi luego pregunta si pertenece al salon de la fama o no
    recibe la lista y el nombre ingresado por el usuario
    '''
    lista_jugador = busqueda_de_nombres(lista_jugadores, nombre)

    try:
        for jugador in lista_jugador:
            flag = False
            for logros in jugador["logros"]:
                if (logros == "Miembro del Salon de la Fama del Baloncesto"):
                    print(
                        "\n---{0}--- Pertenece al salon de la fama\n".format(jugador["nombre"]))
                    flag = True
            if (flag == False):
                print(
                    "\n---{0}--- NO Pertenece al salon de la fama\n".format(jugador["nombre"]))
    except:
        pass

# EJERCICIO 7,8,9


def calcular_max_segun_key(lista: list, key: str):
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
# Permitir al usuario ingresar un valor y mostrar los jugadores que
# han promediado más puntos por partido que ese valor.
# EJERCICIO 10


def mayor_o_menor_que_promedio(lista_jugadores, numero_consulta):
    lista_ordenada = ordenar_por_puntos_promedios(lista_jugadores)
    for persoanje in lista_ordenada:
        if (persoanje["estadisticas"]["promedio_puntos_por_partido"] > numero_consulta):
            print("El jugador {0}, tiene un promedio mayor al que ingresaste : {1}\n".format(
                persoanje["nombre"], persoanje["estadisticas"]["promedio_puntos_por_partido"]))
