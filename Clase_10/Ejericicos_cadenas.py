"""
Crear una función que reciba por parámetro una cadena y un caracter.
La función deberá contar cuántas veces aparece dicho caracter en la cadena y retornar ese valor.

Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.

Crear una función que reciba una cadena y retorne la misma pero al reverso.

Ej: Si recibe la cadena “hola”, deberá retornar “aloh”.

Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.


	Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.
	
Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.

Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.

Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.

Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.

Nota: Todos los ejercicios deben realizarse utilizando el enfoque algorítmico visto durante el transcurso de la cursada.

"""

# 1. Crear una función que reciba por parámetro una cadena y un caracter.
# La función deberá contar cuántas veces aparece dicho caracter en la cadena y retornar ese valor.
def contar_caracteres(cadena: str, caracter: str) -> int:
    
    encontrado = 0

    for i in range(len(cadena)):
        if cadena[i] == caracter:
            encontrado += 1

    return encontrado

print(contar_caracteres("holo", "o"))

#2. Crear una función que reciba una cadena y un caracter. 
#La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.


def retornar_indice(cadena: str, caracter: str) -> int:

    indice = -1
    
    for i in range(len(cadena)):

        if cadena[i] == caracter:
            indice = i
            break
            
    return indice
        

retornar_indice("hola como estan", "o")
        
#3. Crear una función que reciba una cadena y retorne la misma pero al reverso.

def invertir_cadena(cadena: str):

    cadena_invertida = ""
    for i in range(len(cadena) -1, -1, -1):
        
        cadena_invertida += cadena[i]

    return cadena_invertida


print(invertir_cadena("hola como estan"))

#4. Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.


	#Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

def evitar_repeticion(cadena: str) -> str:

    cadena_sin_repetir = ""

    for i in range(len(cadena) - 1):
        if cadena[i] != cadena[i + 1]:
            cadena_sin_repetir += cadena[i]
    
    cadena_sin_repetir += cadena[i + 1]

    return cadena_sin_repetir


print(evitar_repeticion("hooolaaaa"))

#5. Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.

#   Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.



def quitar_vocales(cadena: str) -> str:

    vocales = ["a", "e", "i", "o", "u"]

    cadena_nueva = ""

    cadena = cadena.lower()

    for i in range(len(cadena)):

        bandera = False

        for j in range(len(vocales)):

            if cadena[i] == vocales[j]:

                bandera = True

        if bandera == False:

            cadena_nueva += cadena[i]


    print(cadena_nueva)

quitar_vocales("Hola")


# 6. Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.

#   Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.


# def encontrar_repeticion(cadena: str) -> int:

#     subcadena = ""
#     contador = 0 
#     contador_1 = 0

#     for i in range(len(cadena)):

#         subcadena += cadena[i]

#         for j in range(len (subcadena)):

#             if cadena[i] == subcadena[j]:

#                 for k in range(len(subcadena)):

#                     if cadena[i] == subcadena[k]:

#                         contador += 1
            
#             if contador >= 2:

#                 contador_1 += 1

#     return contador_1


# print(encontrar_repeticion("El pan del panadero"))

# 6. Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.

#   Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.


# def encontrar_repeticion(cadena: str, subcadena: str) -> int:

#     condicion = len(subcadena)



#     for i in range(len(cadena)):

#         contador_1 = 0
       
#         contador = 0 

#         for j in range(len(subcadena)):
           
#             if cadena[i] == subcadena [j]:
            
               
#                contador += 1


#         if condicion == contador:
           
#             contador_1 += 1

#     return contador_1

# print(encontrar_repeticion("El pan del panadero", "pan"))
           
def encontrar_repeticion(cadena: str, subcadena: str) -> int:

    contador = 0

    for i in range(len(cadena)):

        if cadena[i: i + len(subcadena)] == subcadena:

            contador += 1

    return contador

print(encontrar_repeticion("El pan del panadero", "pan"))