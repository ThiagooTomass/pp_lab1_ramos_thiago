
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


def mostrar_jugador_segun_indice(lista_jugadores: list, indice: int, bandera: bool):
    '''
    Esta funcion muestra las estadisticas segund el indice ingresado por el usuario
    recibe la lista de jugadores y el indice

    '''
    lista_estadisticas = []
    for atributo, valor in lista_jugadores[indice]["estadisticas"].items():
        lista_estadisticas.append("{0} : {1}".format(atributo, valor))
        if (bandera == True):
            print("{0} : {1}".format(atributo, valor))
    return lista_estadisticas

# EJERCICIO 3


def guardar_dic_segun_indice(lista_jugadores: list, indice: int):
    '''
    Este es el punto 3 todavia no lo hice
    '''
    nombre_y_posicion = lista_jugadores[indice]["nombre"]
    estadisticas = mostrar_jugador_segun_indice(lista_jugadores, indice, False)
    resultado = "\n".join(estadisticas)
    guardar_archivo("jugador_elejido.csv", "{0}\n{1}".format(
        nombre_y_posicion, resultado))

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


def ordenar_por_nombre_o_posicion(lista_jugadores: list, key: str):
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
            if (jugador[key] > lista[0][key]):
                lista_derecha.append(jugador)
            else:
                lista_izquierda.append(jugador)

    lista_izquierda = ordenar_por_nombre_o_posicion(lista_izquierda, key)
    lista_derecha = ordenar_por_nombre_o_posicion(lista_derecha, key)

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

# EJERCICIO 7,8,9,13,14,19 y 16 como min


def calcular_max__min_segun_key(lista: list, key: str, flag: str):
    '''
    Esta funcion busca y muestra el numero maximo segun su key
    Recibe la lista y la key a evaluar
    '''

    altura_max_inicial = None
    for jugador in lista:
        if (altura_max_inicial is None or jugador["estadisticas"][key] > altura_max_inicial and flag == "mayor" or jugador["estadisticas"][key] < altura_max_inicial and flag == "menor"):
            altura_max_inicial = jugador["estadisticas"][key]
            indice_mas_alto_o_bajo = jugador

    print("El jugador con {0} cantidad de {1} es: {2},son {3}".format(flag, key,
                                                                      indice_mas_alto_o_bajo["nombre"], indice_mas_alto_o_bajo["estadisticas"][key]))
    return indice_mas_alto_o_bajo
# EJERCICIO 10,11,12,15,18,20


def mayor_que_promedio(lista_jugadores: list, numero_consulta: int, key: str):
    '''
    Esta funcion muestra los jugadores que superan el numero ingresado por el usuario
    recibe la lista de jguadores, el numero ingresado por el usuario, y la key a comparar
    '''
    contador = 0
    lista_ordenada = ordenar_por_nombre_o_posicion(lista_jugadores, "nombre")
    for persoanje in lista_ordenada:
        if (persoanje["estadisticas"][key] > numero_consulta):
            print("El jugador {0}, tiene un promedio mayor al que ingresaste : {1}\n".format(
                persoanje["nombre"], persoanje["estadisticas"][key]))
        else:
            contador += 1
    if (contador):
        print("{0}/{1}, No superan el valor que ingresaste".format(contador,
              len(lista_ordenada)))
    else:
        print("Todos superan el numero ingresado")
# EJERCICIO 16


def ejercicio_16(lista_jugadores, min):
    '''
    Esta funcion hace el promedio excluyendo el valor minimo
    recibe la lista de jugadores y el diccionario del valor minimo
    '''
    lista_excluyente = []
    for lista in lista_jugadores:
        if (lista["nombre"] != min["nombre"]):
            lista_excluyente.append(lista)
    promedio = promedio_puntos(
        lista_excluyente, "promedio_puntos_por_partido")
    print("El promedio total sin {0} es: {1}".format(min["nombre"], promedio))

# EJERCICIO 17


def mayor_cantidad_logros(lista_jugadores: list):
    '''
    Esta funcion busca y muestra el numero maximo segun su key
    Recibe la lista y la key a evaluar
    '''

    altura_max_inicial = None
    for jugador in lista_jugadores:
        if (altura_max_inicial is None or len(jugador["logros"]) > altura_max_inicial):
            altura_max_inicial = len(jugador["logros"])
            indice_mas_alto_o_bajo = jugador
    print("El jugador con mayor cantidad de logros es: {0}".format(
        indice_mas_alto_o_bajo["nombre"]))


# DE ACA PARA ABAJO EJERCICIO 23


def ordenar_por_estadisticas(lista_jugadores: list, key: str):
    '''
    Esta funcion ordena en orden ascendente el promedio de puntos por partido
    recibe la lista 
    retorna la lista completa pero ordenada 
    '''

    lista = lista_jugadores[:]
    lista_derecha = []
    lista_izquierda = []
    if len(lista) <= 1:
        return lista
    else:
        for jugador in lista[1:]:
            if (jugador["estadisticas"][key] < lista[0]["estadisticas"][key]):
                lista_derecha.append(jugador)
            else:
                lista_izquierda.append(jugador)

    lista_izquierda = ordenar_por_estadisticas(lista_izquierda, key)
    lista_derecha = ordenar_por_estadisticas(lista_derecha, key)

    return lista_izquierda + [lista[0]] + lista_derecha


def ejercicio_bonus(lista_jugadores: list):
    '''
    Esta funcion calcula y guarda la posicion de cada jugador en 4 estadisticas diferentes
    recibe la lista de jugadores
    '''
    resultado_puntos = ordenar_por_estadisticas(
        lista_jugadores, "puntos_totales")
    resultado_rebotes = ordenar_por_estadisticas(
        lista_jugadores, "rebotes_totales")
    resultado_asistencias = ordenar_por_estadisticas(
        lista_jugadores, "asistencias_totales")
    resultado_robos = ordenar_por_estadisticas(
        lista_jugadores, "robos_totales")

    lista_ordenada_por_nombre = ordenar_por_nombre_o_posicion(
        lista_jugadores, "nombre")
    i_puntos = 1
    i_rebotes = 1
    i_asistencias = 1
    i_robos = 1
    nombres_y_rango = []

    for lista_puntos in (resultado_puntos):
        for lista in lista_ordenada_por_nombre:
            if (lista_puntos["nombre"] == lista["nombre"]):
                nombres_y_rango.append(
                    {"nombre": lista["nombre"], "posicion": i_puntos})

        i_puntos += 1

    for lista_rebotes in resultado_rebotes:
        for lista in lista_ordenada_por_nombre:
            if (lista_rebotes["nombre"] == lista["nombre"]):
                nombres_y_rango.append(
                    {"nombre": lista["nombre"], "posicion": i_rebotes})
        i_rebotes += 1

    for lista_asistencias in resultado_asistencias:
        for lista in lista_ordenada_por_nombre:
            if (lista_asistencias["nombre"] == lista["nombre"]):
                nombres_y_rango.append(
                    {"nombre": lista["nombre"], "posicion": i_asistencias})
        i_asistencias += 1

    for lista_robos in resultado_robos:
        for lista in lista_ordenada_por_nombre:
            if (lista_robos["nombre"] == lista["nombre"]):
                nombres_y_rango.append(
                    {"nombre": lista["nombre"], "posicion": i_robos})
        i_robos += 1

    karl = []
    for jugador in lista_jugadores:
        for elemento in nombres_y_rango:
            if elemento["nombre"] == jugador["nombre"]:
                karl.append(elemento["posicion"])

    subgrupos = [karl[i:i+4] for i in range(0, len(karl), 4)]

    subgrupos_con_nombres = []
    for i in range(len(subgrupos)):
        nombre_jugador = lista_jugadores[i]["nombre"]
        subgrupo_con_nombres = "{0}, {1}".format(nombre_jugador, subgrupos[i])
        subgrupos_con_nombres.append(subgrupo_con_nombres)

    resultado = "\n".join(subgrupos_con_nombres)
    print(resultado)
    guardar_archivo("23_de_jordan.csv", resultado)
