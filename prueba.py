import time

start_time = time.time()

# Tu código aquí
time.sleep(2)  # Ejemplo de código que tarda 2 segundos en ejecutarse

end_time = time.time()
elapsed_time = end_time - start_time

print(f"El tiempo de ejecución fue: {elapsed_time} segundos")



def contar_elementos(path_poema: str)-> dict:
    """La funcion se encarga de contar la cantidad de lineas, palabras y caracteres que contiene un poema (el cual se encuentra dentro de una archivo.txt)

    Args:
        path_poema (str): Recibe por parametro un path (ruta) de tipo str donde se crea el archivo (poema en este caso)

    Returns:
        dict: Retorna un diccionario (de tipo dict) el cual muestra la cantidad de lineas, palabras y caracteres que contiene el poema
    """

    contador_palabras = 0
    contador_lineas = 0
    with open(path_poema, 'r') as archivo:
        poema = archivo.read()
    
    caracteres = len(poema)   

    lista_solo_palabras = poema.split(' ')
    for i in range(len(lista_solo_palabras)):
        contador_palabras += 1


    with open(path_poema, 'r') as archivo:
        lista_con_lineas = archivo.readlines()
        

    for lineas in lista_con_lineas:
        contador_lineas += 1
        

    retorno = {
        "Lineas" : contador_lineas,
        "Palabras" : contador_palabras, 
        "Caracteres" : caracteres
    }
    
    return retorno

print(contar_elementos("Clase_15\practica_archivos\poema.txt"))
