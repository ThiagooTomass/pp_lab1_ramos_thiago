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


def busqueda_de_nombres(lista_jugadores: list, nombre: str):
    '''
    Esta funcion guarda los nombres que tengan un parecido con el nombre ingresado por el usuario
    recibe la lista de jugadores y el nombre ingresado por el usuario
    retoran una lista con los nombres que tengan un parecido
    '''
    lista_segun_nombres = []
    for jugadores in lista_jugadores:
        if re.match(jugadores["nombre"][0:5], nombre[0:5]) != None:
            lista_segun_nombres.append(jugadores)

    if len(lista_segun_nombres) > 0:
        return lista_segun_nombres
    else:
        print("No existe ese nombre")


def promedio_puntos(lista_jugadores: list, key: str):
    '''
    Esta funcion calcula el promedio de los jugadores segun la key
    recibe la lista y la key a calcular
    retorna el valor del promedio
    '''
    acumulador = 0
    for jugador in lista_jugadores:
        acumulador += jugador["estadisticas"][key]
    promedio = acumulador/len(lista_jugadores)
    return promedio


def funcion_numero_por_usuario():
    '''
    Esta funcion chequea que el numero ingresado por el usuairo este correcto
    '''
    numero_a_preguntar = input("Ingrese numero para comparar: ")
    if (numero_a_preguntar.isdigit()):
        numero_a_preguntar = int(numero_a_preguntar)
        if (numero_a_preguntar > 0):
            return numero_a_preguntar
        else:
            print("Tiene que ingresar un numero positivo")
    else:
        print("Tiene que ingresar solo numeros")


def printear_ordenamiento(lista_ordenada: list, key: str):
    '''
    Esta funciona printea una lista ordenada
    recibe la lista ya ordenada y la key a printear
    '''
    i = 1
    for jugador in lista_ordenada:
        print("{0}-{1}:  {2}".format(i,
                                     jugador["nombre"], jugador["estadisticas"][key]))
        i += 1
