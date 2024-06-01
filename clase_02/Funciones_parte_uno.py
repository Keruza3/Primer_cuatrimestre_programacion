import math

"""
Funciones Parte I

1. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
2. Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
3. Crear una función que le solicite al usuario el ingreso de una cadena y la retorna.
4. Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables (que reciban el mensaje de pedido de datos por parámetro). Agregar validaciones.
5. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
6. Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
7. Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
8. Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

"""

#punto 1

def ingresar_entero() ->int:
    """ Se ingresa el numero entero
        no acepta parametros
        devuelve el numero entero
    """
    
    numero_entero = int(input("Ingrese un numero entero: "))

    return numero_entero



#punto 2

def ingresar_flotante() -> float:
    """ Se ingresa el numero flotante
        no acepta parametros
        devuelve el numero flotante
    """


    numero_flotante = float(input("Ingrese un numero flotante: "))

    return numero_flotante

#punto 3

def ingresar_cadena(cadena) -> str:
    """ Se ingresa el texto
        no acepta parametros
        devuelve el texto
    """
    cadena = str(input("Ingrese un texo: "))

    return cadena

#punto 4


def solicitar_entero_especializado(mensaje:str,  rango_1:int , rango_2:int) -> int:
    """ toma un mensaje y lo muestra, con la informacion lo verificia en un rango especifico
        acepta 3 parametros:
        - Mensaje: un mensaje
        - Rango_1: es el rango minimo deseado
        - Rango_2: es el rango maximo deseado 
        devuelve el numero ingresado ya verificado
    """
    numero = int(input(mensaje))

    while numero < rango_1 or numero > rango_2:
        
        numero = int(input(mensaje))
    
    return numero

mensaje = "Ingrese su edad: "

rango_1 = 1
rango_2 = 110

solicitar_entero_especializado(mensaje , rango_1 , rango_2)

def solicitar_numero_flotante_especializado(mensaje:str , rango_1:int , rango_2:int) -> int:
    """
    toma un mensaje y lo muestra, con la informacion lo verifica en un rango especifico
    
    acepta 3 parametros:

    - Mensaje: un mensaje
    - Rango_1: es el rango minimo deseado
    - Rango_2: es el rango maximo deseado

    devuelve el numero ingresado ya verificado()

    """


    numero = float(input(mensaje))

    while numero < rango_1 or numero > rango_2:

        numero = float(input(mensaje))

    return numero
    
mensaje = "Ingrese su peso (ej. 70.3): "

rango_1 = 0
rango_2 = 170.9

solicitar_numero_flotante_especializado(mensaje , rango_1 , rango_2)

def solicitar_cadena_especializado (mensaje:str , parametro_1:str , parametro_2:str) -> str:
    """
    toma un mensaje y lo muestra, con la informacion lo verificia en entre distintas posibles respuestas
    acepta 2 parametros(pero pueden ser mas):

    - Mensaje: un mensaje
    - parametro_1: posible respuesta
    - parametro_2: posible respuesta

    devuelve la respuesta ya ya verificado
    """


    mensaje_usuario = input(mensaje)

    mensaje_usuario = mensaje_usuario.upper()


    while mensaje_usuario != parametro_1 and mensaje_usuario !=parametro_2:

        mensaje_usuario = input(mensaje)

        mensaje_usuario = mensaje_usuario.upper()

        return mensaje_usuario

mensaje = "usted es mayor de edad? Porfavor responda con si o no: "

parametro_1 = "SI"
parametro_2 = "NO"


solicitar_cadena_especializado(mensaje , parametro_1 , parametro_2)

#punto 5

def calculo_area_circulo(radio:float) -> float:
    """
    esta funciona calcula el area de un circulo, con un radio ingresado

    parametros:
    radio: el valor ingresado del radio

    devuelve el valor del area
    """

    area = math.pi * radio ** 2

    return area


radio = float(input("Ingrese el radio: "))

calculo_area_circulo(radio)

#punto 6

def verificar_par_impar() -> None:
    """
    La funcion verifica si un numero es par o impar 
    No acepta parametros
    devuelve un mensaje diciendo

    """

    numero_ingresado = int(input("Ingrese un numero para ver si es par o no: "))

    resultado = numero_ingresado % 2

    if resultado == 0:
       
       mensaje = f"El numero {numero_ingresado} es par"
    
    else:
        
        mensaje = f"El numero {numero_ingresado} es impar"

    print(mensaje)

verificar_par_impar()


  #punto 7

def maximo_numero() ->  float:

    """
    Esta funcion saca el maximo numero de tres ingresados

    no acepta parametros

    devuelve el numero maximo ingresado

    """
    
    numero_1 = float(input("Ingrese el primer numero: "))
    
    numero_2 = float(input("Ingrese el segundo numero: "))
    
    numero_3 = float(input("Ingrese el tercer numero: "))
    
    
    if numero_1 > numero_2 and numero_1 > numero_3:
        
        return numero_1
    
    else:
        
        if numero_2 > numero_1 and numero_2 > numero_3:
            
            return numero_2
        
        else:
            
            return numero_3
        
#maximo_numero()

    #punto 8

def potenciacion(base:float , exponente:float) -> float:
    """
    Esta funcion hace la potencia del numero base ingresado con el exponente ingresado
    
    acepta 2 parametros:

    -base: la base
    -exponente: el exponente

    devuelve el resultado de la potenciacion
    
    """

    resultado = base ** exponente

    return resultado

base = float(input("Ingrese una base: "))

exponente = float(input("Ingrese un exponente para la base: "))

potenciacion(base , exponente)
