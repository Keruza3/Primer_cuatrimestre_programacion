"""
Crear una función que reciba como parámetros una lista de números y el path de un archivo. 
La misma deberá guardar la lista en un archivo de texto.
"""

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def guardar_lista_int_txt(lista_numeros:list[int], path_archivo:str) -> None:
    """Recibe un path para almacenar una lista de numeros en la direccion recibida

    Args:
        - lista_numeros (list[int]): lista numeros
        - path_archivo (str): El path donde se va a crear el archivo nuevo
    """

    with open(path_archivo, "w") as archivo:

     

            linea = str(linea)

            archivo.write(f"{linea}\n")

# guardar_lista_int_txt(lista_numeros, "Clase_15/practica_archivos/punto_1.txt")

"""
Crear una función que reciba como parámetro el path de un archivo.
La misma deberá leer el archivo del ejercicio anterior, solo dejando pasar a la lista los números múltiplos de 2.
"""

def revisar_lista_multiplos(path_archivo:str) -> bool:
    """Esta funcion recorre el archivo(que tiene que tener solo numeros) recibido por path y pone en una lista los numeros multiplos de 2 e imprime la lista

    Args:
        path_archivo (str): un archivo que solo tiene numeros

    Returns:
        bool: si es true es que tiene por lo menos un multiplo de 2, false si ningun numero cumple la condicion
    """

    lista_nueva = []

    contador = 0

    retorno = False

    with open(path_archivo, "r") as archivo:

        lista = archivo.readlines()

    for numero in lista:

        numero = numero.replace("\n","")

        numero = int(numero)

        if numero % 2 == 0:

            lista_nueva.append(numero)

            contador += 1

    if contador == 0:

        mensaje = "En la lista ingresada ningun numero es multiplo de 2"

        print(mensaje)

    else: 

        mensaje = f"\nEn la lista ingresada hay {contador} numeros que son multiplos de 2\n"

        print(mensaje)

        print(f"{lista_nueva}")

        retorno = True

    return retorno

# revisar_lista_multiplos("Clase_15\practica_archivos\punto_1.txt")

"""
Crear una función que reciba como parámetros dos paths: uno correspondiente a un archivo de origen y otro correspondiente a un archivo de destino. 
La función debe leer el contenido del archivo de origen y luego transcribirlo en el archivo de destino. 
En caso de error la función retornará algún tipo de código de error indicando que paso.
"""

def pasar_informacion(path_origen: str, path_destino: str) -> str:
    """Esta función recibe un path origen El cual hace referencia al archivo origen y recibe por otro lado el path destino, 
    el cuál es donde se va almacenar el el nuevo archivo y pasa la información del pat origen al path destino

    Args:
        path_origen (str): archivo a buscar
        path_destino (str): donde se va guardar el archivo

    Returns:
        _type_: En el caso que hay un error este se huele como mensaje
    """
    verificar_path = path_origen.split(".")

    verificar_path_1 = path_destino.split(".")

    retorno = ""

    if verificar_path[1] == "txt" and verificar_path_1[1] == "txt":

        
        with open(path_origen, "r") as archivo:

            informacion = archivo.read()

        if informacion == "" or informacion == [] or informacion == {}:

            retorno += f"\n El path {path_origen} ingresado tiene informacion vacia, no se puede pasar información vacia"

        if type(informacion) == str:

            with open(path_destino, "w") as archivo:

                archivo.write(informacion)

        else:

            if type(archivo) == list or type(archivo) == dict:

                with open(path_destino, "w") as archivo:

                    archivo.writelines(informacion)

            else:
            
                retorno += f"\n El tipo de informacion que contiene {path_origen} es invalido"

        retorno = f"Se transcribio el archivo correctamente"


    else:
        
        retorno += f"El archivo no es un tipo .txt, el archivo es invalido"
        
    return retorno

print(pasar_informacion("Clase_15\practica_archivos\poema.txt", "Clase_15\practica_archivos\punto_2.txt"))

"""
Crear una función llamada contar_elementos que recibe como parámetro el path de un archivo de texto que contiene un poema. 
La función deberá contar la cantidad de líneas, la cantidad de palabras y la cantidad de caracteres que contiene el poema.
La función retornará un diccionario con los datos obtenidos.
"""

def contar_elementos(path_poema: str) -> dict:
    """Esta función recibe un path de un poema y esta devuelve por diccionario los caracteres del poema y las palabras que tiene el poema
    
    Args:
        path_poema (str): Path del poema recibido

    Returns:
        dict:  devuelve por diccionario los caracteres del poema y las palabras que tiene el poema
    """

    contador_palabras = 0
    contador_lineas = 0

    with open(path_poema, "r", encoding = "UTF-8") as archivo:

        poema  = archivo.read()

            
    with open(path_poema, "r", encoding = "UTF-8") as archivo:

        lineas = archivo.readlines()

        for i in range(len(lineas)):
    
            contador_lineas += 1

    caracteres = len(poema)

    poema = poema.replace("\n", " ")

    poema = poema.split(" ")

    for palabra in poema:

        contador_palabras += 1

    diccionario_poema = {"palabras" : contador_palabras,
                        "caracteres" : caracteres,
                        "lineas": contador_lineas}
    
    return diccionario_poema

    
# print(contar_elementos("Clase_15\practica_archivos\poema.txt"))