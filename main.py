from funciones import *
import json


def parse_json(nombre_archivo: str):
    lista_jugadores = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        dict = json.load(archivo)
        lista_jugadores = dict["jugadores"]

    return lista_jugadores


ruta_archivo = r"C:\Users\thiag\OneDrive\Escritorio\Primer cuatri\EXAMEN.py\dt.json"
lista_jugadores = parse_json(ruta_archivo)

while True:
    opcion = input("Ingrese opcion: ")

    if (opcion == "1"):
        mostrar_nombre_posicion(lista_jugadores)

    elif (opcion == "2"):
        indice = input("Ingrese indice de jugador: ")
        indice = int(indice)

        if (indice >= 0 and indice < len(lista_jugadores)):
            mostrar_jugador_segun_indice(lista_jugadores, indice)
    elif (opcion == "3"):
        guardar_dic_segun_indice(lista_jugadores, indice)

    elif (opcion == "4"):
        nombre = input("Ingrese nombre de jugador: ").lower().capitalize()
        buscar_por_nombre(lista_jugadores, nombre)

    elif (opcion == "5"):
        promedio = promedio_puntos(
            lista_jugadores, "promedio_puntos_por_partido")
        print("El promedio del Dream Team por partido es: {0}".format(
            promedio))

        resultado = ordenar_por_puntos_promedios(lista_jugadores)
        i = 1
        for jugador in resultado:
            print("{0}-{1}".format(i,
                                   jugador["estadisticas"]["promedio_puntos_por_partido"]))
            i += 1

    elif (opcion == "6"):
        nombre = input("Ingrese nombre de jugador: ").lower().capitalize()
        salon_de_la_fama(lista_jugadores, nombre)

    elif (opcion == "7"):
        calcular_max_segun_key(
            lista_jugadores, "rebotes_totales")
    elif (opcion == "8"):
        calcular_max_segun_key(lista_jugadores,
                               "porcentaje_tiros_de_campo")
    elif (opcion == "9"):
        calcular_max_segun_key(lista_jugadores,
                               "asistencias_totales")
    elif (opcion == "10"):
        numero_a_preguntar = input("Ingrese numero para comparar: ")
        numero_a_preguntar = int(numero_a_preguntar)
        if (numero_a_preguntar > 0):
            mayor_o_menor_que_promedio(lista_jugadores, numero_a_preguntar)
        else:
            print("Tiene que ingresar un numero positivo")
    elif (opcion == "z" or opcion == "Z"):
        print("Saliste del programa")
        break

    input("Apriete enter para seguir ")
