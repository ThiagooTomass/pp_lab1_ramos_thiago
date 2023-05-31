
from funciones_interactivas import *

# EJERCICIO 1


def mostrar_nombre_posicion(lista_jugadores: list):
    '''
    Esta funcion imprime el nombre y posicion de los jugadores del dream team
    recibe la lista y no terona nada
    '''

    for jugador in lista_jugadores:
        print("{0} - {1}".format(jugador["nombre"], jugador["posicion"]))

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


def ordenar_por_nombre_o_posicion(lista_jugadores: list, key: str, opcion: bool):
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
            if ((opcion == True and jugador[key] > lista[0][key]) or
                    (opcion == False and jugador["estadisticas"][key] < lista[0]["estadisticas"][key])):
                lista_derecha.append(jugador)
            else:
                lista_izquierda.append(jugador)

    lista_izquierda = ordenar_por_nombre_o_posicion(
        lista_izquierda, key, opcion)
    lista_derecha = ordenar_por_nombre_o_posicion(lista_derecha, key, opcion)

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
        if (altura_max_inicial is None or jugador["estadisticas"][key] > altura_max_inicial and flag == "mayor" or
                jugador["estadisticas"][key] < altura_max_inicial and flag == "menor"):
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
    lista_ordenada = ordenar_por_nombre_o_posicion(
        lista_jugadores, "nombre", True)
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


def calcular_posicion_rankin(lista: list):
    '''
    Esta funcion ordena la lista por 4 estadisticas diferentes y muestra un ranking de los jugadores

    recibe la lista de jugadores 
    '''
    if (lista):
        jugadores_auxiliar = lista[:]

        lista_auxiliar_puntos = ordenar_por_nombre_o_posicion(
            jugadores_auxiliar, "puntos_totales", False)

        lista_auxiliar_rebotes = ordenar_por_nombre_o_posicion(
            jugadores_auxiliar, "rebotes_totales", False)

        lista_auxiliar_asistencias = ordenar_por_nombre_o_posicion(
            jugadores_auxiliar, "asistencias_totales", False)

        lista_auxiliar_robos = ordenar_por_nombre_o_posicion(
            jugadores_auxiliar, "robos_totales", False)

        jugadores_datos = ["Jugador,Puntos,Rebotes,Asistencias,Robos"]
        for jugador in lista:

            dato_jugador = []

            indice_puntos = (lista_auxiliar_puntos.index(jugador))+1
            indice_rebotes = (lista_auxiliar_rebotes.index(jugador))+1
            indice_asistencias = (lista_auxiliar_asistencias.index(jugador))+1
            indice_robos = (lista_auxiliar_robos.index(jugador))+1

            dato_jugador.append(jugador["nombre"])
            dato_jugador.append(str(indice_puntos))
            dato_jugador.append(str(indice_rebotes))
            dato_jugador.append(str(indice_asistencias))
            dato_jugador.append(str(indice_robos))

            dato_jugador = ",".join(dato_jugador)
            jugadores_datos.append(dato_jugador)

        datos_para_csv = "\n".join(jugadores_datos)
        guardar_archivo("ejercicio_23.csv", datos_para_csv)


def examne_parcial_extra(lista_jugadores: list):
    '''
    Esta funcion muestra la cantidad de posiciones que hay entre los jugadores
    recibe la lista de jugadores
    '''
    lista_nueva = {}
    for jugador in lista_jugadores:
        if jugador["posicion"] == "":
            jugador["posicion"] = "La lista se encuentra vacía"
        valor = jugador["posicion"].capitalize()
        if valor in lista_nueva:
            lista_nueva[valor] += 1
        else:
            lista_nueva[valor] = 1
    for atributo, valor in lista_nueva.items():
        print("{0} : {1}".format(atributo, valor))


def examne_parcial_extrav2(lista_jugadores: list):
    '''
    Esta funcion extrae el numero de los all-star, los ordena y los imprime

    recibe la lista de jugadores
    '''
    lista_con_nombres_all_star = []
    for cadena in lista_jugadores:
        for i in range(len(cadena["logros"])):
            if re.search(r"All-Star$", cadena["logros"][i]):
                logros_numeros = re.sub(r'[^0-9]', '', cadena["logros"][i])
                posicion = int(logros_numeros)
                diccionario = {
                    "nombre": cadena["nombre"],
                    "posicion": posicion
                }
                lista_con_nombres_all_star.append(diccionario)
    valores_ordenados = ordenar_por_nombre_o_posicion(
        lista_con_nombres_all_star, "posicion", True)
    for resultado in valores_ordenados:
        nombre = resultado["nombre"]
        posicion = resultado["posicion"]
        print("{0} ({1} veces All-Star)".format(nombre, posicion))


def examne_parcial_extrav3(lista_jugadores: list):
    '''
    Esta funcion muestra el mayor de todas las key de estadisticas
    recibe la lista de jugadores
    '''
    for tipos_estadisticas in lista_jugadores[0]["estadisticas"]:
        calcular_max__min_segun_key(
            lista_jugadores, tipos_estadisticas, "mayor")
