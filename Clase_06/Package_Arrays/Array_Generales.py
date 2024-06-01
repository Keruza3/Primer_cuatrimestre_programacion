from Package_Input.Input import get_int
from .Especificas import determinar_positividad, validar_paridad, mostrar_lista


lista = [-1] * 10

def seleccionar_a(lista:list) -> None:
    """Pide 10 numeros y los ingresa en una lista

    Args:
        lista (list): Lista vacia
    """

    for i in range(len(lista)):
        lista[i] = get_int("Ingrese 10 numeros: ", "Numero erroneo: ", -1000, 1000, 3)

#---------------------------------------------------------------------------------------------

def contador_positivos_negativos(lista: list)-> None:
    """Muestra la cantidad de numeros de numeros y negativos

    Args:
        lista (list): lista predefinida
    """

    
    contador_positivos = 0
    contador_negativos = 0
    for i in range(len(lista)):
        if determinar_positividad(lista[i]) == True:
            contador_positivos += 1
        elif determinar_positividad(lista[i]) == False:
            contador_negativos += 1

    print(f"La cantidad de positivos es {contador_positivos}, la cantidad de negativos es {contador_negativos}")

#---------------------------------------------------------------------------------------------

def sumar_pares (lista: list)-> None:
    """Suma los numeros pares

    Args:
        lista (list): lista predefinida
    """


    acumulador_pares = 0
    for i in range (len(lista)):
        if validar_paridad(lista[i]) == True:
            acumulador_pares += lista[i]
    
    print(f"la sumatoria de los números pares es: {acumulador_pares}")

#---------------------------------------------------------------------------------------------

def mayor_impar(lista:list)-> None:
    """Imprime el mayor numero impar

    Args:
        lista (list): lista predefinida
    """


    impar_mayor = 0

    for i in range(len(lista)):

       if validar_paridad(lista[i]) == False:
           
           if i == 1 or lista[i] > impar_mayor:
                
                impar_mayor = lista[i]
            

    print(f"El numero impar mayor es: {impar_mayor}")

#---------------------------------------------------------------------------------------------

def listar_numeros(lista:list)-> None:
    """Muestra los numeros numeros de una lista

    Args:
        lista (list): lista predefinida
    """


    print("los numeros ingresados en la lista son: ")

    mostrar_lista(lista)

#---------------------------------------------------------------------------------------------

def listar_impares(lista:list)-> None:
    """ Muestra la cantidad de numeros impares que hay en la lista

    Args:
        lista (list): lista predefinida
    """



    print("los numeros impares ingresados en la lista son: ")

    for i in range(len(lista)):
        
        if validar_paridad(lista[i]) == False:
            print(lista[i])

#---------------------------------------------------------------------------------------------

def listar_indice_impar(lista:list)-> None:
    """Muestra los indices de los numeros pares de la lista

    Args:
        lista (list): lista predefinida
    """


    print("los indices de los numeros impares ingresados en la lista son: ")

    for i in range(len(lista)):

        if validar_paridad(lista[i]) == False:
            print(i)

#---------------------------------------------------------------------------------------------