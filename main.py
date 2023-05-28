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
flag = True
while True:
    opcion = input("Ingrese opcion: ")

    if (opcion == "1"):

        mostrar_nombre_posicion(lista_jugadores)

    elif (opcion == "2"):

        indice = input("Ingrese indice de jugador: ")
        if (indice.isdigit()):
            indice = int(indice)
            if (indice >= 0 and indice < len(lista_jugadores)):
                mostrar_jugador_segun_indice(lista_jugadores, indice, True)
            else:
                print("Ingreso mal la opcion")
        else:
            print("Primero ejecuta el 2")
        flag = False

    elif (opcion == "3"):

        if (flag == False):
            guardar_dic_segun_indice(lista_jugadores, indice)
        else:
            print("Para ejecutar la opcion 3 debe ejecutarse primero la opcion 2")

    elif (opcion == "4"):

        nombre = input("Ingrese nombre de jugador: ").lower().capitalize()
        buscar_por_nombre(lista_jugadores, nombre)

    elif (opcion == "5"):

        promedio = promedio_puntos(
            lista_jugadores, "promedio_puntos_por_partido")
        print("El promedio del Dream Team por partido es: {0}".format(
            promedio))

        resultado = ordenar_por_nombre_o_posicion(lista_jugadores, "nombre")
        printear_ordenamiento(resultado, "promedio_puntos_por_partido")

    elif (opcion == "6"):

        nombre = input("Ingrese nombre de jugador: ").lower().capitalize()
        salon_de_la_fama(lista_jugadores, nombre)

    elif (opcion == "7"):

        calcular_max__min_segun_key(
            lista_jugadores, "rebotes_totales", "mayor")

    elif (opcion == "8"):

        calcular_max__min_segun_key(lista_jugadores,
                                    "porcentaje_tiros_de_campo", "mayor")

    elif (opcion == "9"):

        calcular_max__min_segun_key(lista_jugadores,
                                    "asistencias_totales", "mayor")

    elif (opcion == "10"):

        numero_ingresado = funcion_numero_por_usuario()
        mayor_que_promedio(
            lista_jugadores, numero_ingresado, "promedio_puntos_por_partido")

    elif (opcion == "11"):

        numero_ingresado = funcion_numero_por_usuario()
        mayor_que_promedio(
            lista_jugadores, numero_ingresado, "promedio_rebotes_por_partido")

    elif (opcion == "12"):

        numero_ingresado = funcion_numero_por_usuario()
        mayor_que_promedio(
            lista_jugadores, numero_ingresado, "promedio_asistencias_por_partido")

    elif (opcion == "13"):

        calcular_max__min_segun_key(lista_jugadores,
                                    "robos_totales", "mayor")
    elif (opcion == "14"):

        calcular_max__min_segun_key(lista_jugadores,
                                    "bloqueos_totales", "mayor")
    elif (opcion == "15"):

        numero_ingresado = funcion_numero_por_usuario()
        mayor_que_promedio(
            lista_jugadores, numero_ingresado, "porcentaje_tiros_libres")

    elif (opcion == "16"):

        min = calcular_max__min_segun_key(lista_jugadores,
                                          "promedio_puntos_por_partido", "menor")
        ejercicio_16(lista_jugadores, min)

    elif (opcion == "17"):

        mayor_cantidad_logros(lista_jugadores)

    elif (opcion == "18"):

        numero_ingresado = funcion_numero_por_usuario()
        mayor_que_promedio(
            lista_jugadores, numero_ingresado, "porcentaje_tiros_triples")

    elif (opcion == "19"):

        calcular_max__min_segun_key(
            lista_jugadores, "temporadas", "mayor")

    elif (opcion == "20"):

        numero_ingresado = funcion_numero_por_usuario()
        valores_ordenados = ordenar_por_nombre_o_posicion(
            lista_jugadores, "posicion")
        mayor_que_promedio(valores_ordenados, numero_ingresado,
                           "porcentaje_tiros_de_campo")
    elif (opcion == "23"):

        ejercicio_bonus(lista_jugadores)

    elif (opcion == "24"):
        print("Saliste del programa")
        break

    input("Apriete enter para seguir ")
