def  determinar_positividad(number: int)->bool:
    """Determina si un numero es positivo o no

    Args:
        number (int): Numero ingresado

    Returns:
        bool: Verdaredo (positivo) o falso (negativo)
    """

    retorno = None
    if number > 0:
        retorno = True
    elif number < 0:
        retorno = False
    
    return retorno

#---------------------------------------------------------------------------------------------

def validar_paridad (numero: int)-> bool:
    """Verifica si un numero es par o no


    Args:
        numero (int): numero ingresado

    Returns:
        bool: Verdaredo (par) o falso (impar)
    """
    par = False
    if numero % 2 == 0:
        par = True
    
    return par

#---------------------------------------------------------------------------------------------

def mostrar_lista(lista:list)-> None:
    """Muestra una lista y la imprime

    Args:
        lista (list): lista predefinida
    """

    for i in range(len(lista)):
        print(lista[i])
