import math

"""
Arrays Unidimensionales

1 Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
2 Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
3 Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
4 Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
5 Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
6 Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. 
La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.
"""

lista = [1, 3, 56, -78, 89, 3, -2, 89]

def promedio_lista_enteros (lista:list) -> int | float:
    """función que reciba una lista de enteros, la misma calculará

    Args:
        lista (list): Lista predefenida

    Returns:
        int | float: devuelve el promedio de todos los numeros
    """

    acumulador = 0

    for i in range(len(lista)):

        acumulador += lista[i]

    promedio = acumulador / (len(lista))
    promedio = round(promedio)

    return promedio

print(promedio_lista_enteros(lista))

def promedio_positvos(lista:list) -> int | float:
    """calcula el promedio de solo los numeros positivos

    Args:
        lista (list): lista predefinida
    Returns:
        int | float: Devuelve el promedio 
    """
    
    
    acumulador = 0
    numeros_positivos = 0

    for i in range(len(lista)):
        
        if lista[i] > 0:
            acumulador += lista[i]
            numeros_positivos += 1


    promedio = acumulador / numeros_positivos

    return promedio

#3 Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

def multiplicacion_lista(lista:list) -> int:
    """Calcula el producto de todos los elementos

    Args:
        lista (list): lista predefinida

    Returns:
        int: el producto de todos los numeros
    """
    producto_final = 1

    for i in range(len(lista)):

        producto_final *= lista[i]

    return producto_final

print(multiplicacion_lista(lista))


# 4 Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

def encontrar_maximo(lista:list) -> int:
    """Encuentra el numero maximo de una lista 

    Args:
        lista (list): lista predefinida

    Returns:
        int: devuelve la posicion del numero maximo
    """


    for i in range(len(lista)):
        
        if i == 0 or lista[i] > numero_maximo:

            numero_maximo = lista[i]
            posicion = i
             

    return posicion
    
print(encontrar_maximo(lista))

#5 Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.


def encontrar_varios_maximos(lista:list) -> None:
    """Encuentra un numero maximo y si hay iguales los printea

    Args:
        lista (list): lista predefinida

    Returns:
            Devuelve none   
    """

    for i in range(len(lista)):
        
        if i == 0 or lista[i] > numero_maximo:

            numero_maximo = lista[i]

    for i in range(len(lista)):
    
        if numero_maximo == lista[i]:
            
            posicion = i+1

            print(f"Se encontro un numero igual en la posicion: {posicion}")


encontrar_varios_maximos(lista)
    

#6 Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. 
#La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.

lista_nombres = ["Mati", "Juani", "Thiago", "Santi"]


def reemplazar_nombres(lista_nombres:list, buscar:str, reemplazar:str) -> int:
    """Encuentra y reeemplaza nombres y marca los cambios que se hicieron

    Args:
        lista_nombres (list): Lista predefinida
        buscar (str): El nombre a buscar
        reemplazar (str): El nombre que se quiere poner al reemplazar

    Returns:
        int: devuelve la cantidad de cambios
    """
    
    cambios = 0
    
    for i in range(len(lista_nombres)):
        
        if lista_nombres[i] == buscar:
            lista_nombres[i] = reemplazar
            cambios += 1

    return cambios
    
print(reemplazar_nombres(lista_nombres, "Santi", "Mati"))
    

        
