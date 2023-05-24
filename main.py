from funciones import *
import json


def parse_json(nombre_archivo: str):
    lista_jugadores = []
    with open(nombre_archivo, "r") as archivo:
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
        nombre = input("Ingrese nombre de jugador: ")
        buscar_por_nombre(lista_jugadores, nombre)
    elif (opcion == "4"):
        pass
    elif (opcion == "z" or opcion == "Z"):
        print("Saliste del programa")
        break

    input("Apriete enter para seguir ")
