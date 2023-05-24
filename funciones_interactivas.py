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
