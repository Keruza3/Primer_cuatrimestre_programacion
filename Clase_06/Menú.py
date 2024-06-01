from Package_Arrays.Array_Generales import *


validar = False

while True:
    print("""Elija una de las siguientes opciones: 
    A. Pedir el ingreso de 10 números enteros entre -1000 y 1000.
    B. Mostrar la cantidad de números positivos y negativos.
    C. Mostrar la sumatoria de los números pares.
    D. Informar el mayor de los números impares.
    E. Listar todos los números ingresados.
    F. Listar todos los números pares.
    G. Listar los números de las posiciones impares. 
    H. Salir. """)

    opcion = input("")
    opcion = opcion.upper()

    match(opcion):
        case "A": 

            seleccionar_a(lista)
            validar = True

        case "B":
           
            if validar == True :
                contador_positivos_negativos(lista)

            else:
                print("No se ingresaron datos en el punto A")

        case "C":
            
            if validar == True :
                sumar_pares(lista)

            else:
                print("No se ingresaron datos en el punto A")

        case "D":
            
            if validar == True :
                mayor_impar(lista)

            else:
                print("No se ingresaron datos en el punto A")

            
        case "E":
            
            if validar == True :
                listar_numeros(lista)

            else:
                print("No se ingresaron datos en el punto A")

        case "F":
          
            if validar == True :
                listar_impares(lista)

            else:
                print("No se ingresaron datos en el punto A")
    
        case "G":
            
            if validar == True :
                listar_indice_impar(lista)

            else:
                print("No se ingresaron datos en el punto A")

        case "H":

            break #corta el while -> sale del bucle

        case _:
            opcion = input("Ingrese una opcion válida: ")