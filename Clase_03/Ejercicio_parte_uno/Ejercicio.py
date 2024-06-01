
#EJERCICIO 1

def conseguir_entero(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int | None:
    
    print(mensaje)

    for _ in range (reintentos):

        numero_ingresado = int(input(""))

        if numero_ingresado < minimo or numero_ingresado > maximo:
            
            print(mensaje_error)


        else:
            
            return numero_ingresado


mensaje = "Ingrese un numero entre 1 y 7 (Tiene 3 intentos)"

mensaje_error = "No ingreso un numero en ese rango, intente nuevamente"

minimo = 1

maximo = 7

reintentos =  3

#conseguir_entero(mensaje, mensaje_error, minimo, maximo, reintentos)



def conseguir_flotante(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> float | None:
    
    print(mensaje)

    for _ in range (reintentos):
        
        numero_ingresado = float(input(""))

        if numero_ingresado < minimo or numero_ingresado > maximo:
            
            print(mensaje_error)
            

        else:
            
            return numero_ingresado

mensaje = "Ingrese un numero entre 0.1 y 0.10 (Tiene 3 intentos)"

mensaje_error = "No ingreso un numero en ese rango, intente nuevamente"

minimo = 0.1

maximo = 0.9

reintentos =  3

conseguir_flotante(mensaje, mensaje_error, minimo, maximo, reintentos)

#Ejercicio 2

def conseguir_string(mensaje:str, mensaje_error:str, longitud:int, reintentos: int) -> str | None:

    print(mensaje)

    for _ in range(reintentos): 
       
        palabra = len(input(""))


        if palabra != longitud:
            print(mensaje_error)

        else:
            return palabra

mensaje = "Intente escribir una palabra que coincida con una cadena de caracteres preestablecida, tiene 10 intentos"

mensaje_error = "La cantidad de caracteres es incorrecta, intente nuevamente"

longitud = 5

reintentos = 10

print(conseguir_string(mensaje, mensaje_error, longitud, reintentos))
