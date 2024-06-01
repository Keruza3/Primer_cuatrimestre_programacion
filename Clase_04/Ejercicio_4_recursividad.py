from Package_Input.Input import get_int

#EJERCICIO 1
#Realizar una función recursiva que calcule la suma de los primeros números naturales (todos los números anteriores al recibido por parámetro):

def sumar_naturales(numero: int) -> int:
    """Se ingresa un muero y la funcion suma todos sus numeros anteriores

    Args:
        numero (int): El numero ingresado

    Returns:
        int: devuelve el numero con ya suma ya hecha 
    """

    if numero == 0:
        
        return numero
    
    return numero + sumar_naturales(numero - 1)

numero = get_int("Ingrese un muemero natural para saber la suma de sus numeros anteriores", "El numero ingresado es invalido", 0, 100000000, 3)

print(sumar_naturales(numero))

#EJERCICIO 2 


def calcular_potencia(base:int , exponente:int) -> int:
    """Esta funcion hace la potencia de un numero ingresado al exponente ingresado

    Args:
        base (int): El numero base
        exponente (int): El exponente que se le quiere poner al numero

    Returns:
        int: Devuelve el numero ya potenciado
    """

    if exponente == 0:
        return 1
    
    return base *  calcular_potencia(base, exponente - 1)

# base = get_int("Ingrese un numero base", "El numero es invalido", 0 , 10000000, 3)

# exponete = get_int("Ingrese el exponente", "El numero es invalido", 0, 1000000, 3)

# print(calcular_potencia(base , exponete))

#EJERCICIO 3

def sumar_digitos(numero: int) -> int:
    
    if numero < 10:
        return numero
    
    fraccion = numero % 10

    numero = numero // 10

    suma = fraccion + sumar_digitos(numero)

    




#numero = get_int("Ingrese un numero para sumar sus digitos", "El numero es invalido", 0 , 10000000, 3)

print(sumar_digitos(22))