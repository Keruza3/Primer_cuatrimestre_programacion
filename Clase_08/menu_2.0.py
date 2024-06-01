
from calculos import *
from validaciones_de_líneas_y_coches import *
from recaudos import *
from extras import *
from generacion_y_verificacion_de_existencia_de_legajo import *
from matrices import *


"""
Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
 
Menú:

Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). 

Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer está asignado a una única línea y coche), 
estos datos deben estar validados. Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). 
Cada coche de cada línea puede tener varias recaudaciones diarias.

Mostrar la recaudación de todos los coches y líneas.

Calcular y mostrar recaudación por línea.

Calcular y mostrarla recaudación total.

Salir
Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y verificación de existencia de legajo, cálculos, etc.
"""



while True: 

    menu = print("""
        A)Cargar planilla         
        B)Mostrar la recaudación de todos los coches y líneas.
        C)Calcular y mostrar recaudación por línea.
        D)Calcular y mostrar recaudación por coche.
        E)Calcular y mostrar la recaudación total.
        F)Salir""")

    bandera_validar = False

   
    opcion = input("Elegir una de estas opciones: ")

    opcion = opcion.upper()

    match opcion:
        case "A": 
                
            print("\nLegajos")
            crear_legajos(matriz_choferes)
            

            while True:
                mostrar_matriz(matriz_choferes)
                print("\nLineas e internos de colectivos")
                mostrar_matriz(matriz_colectivo)

                while validar_legajo(matriz_choferes) == False:
                    print("")

                almacenar_recaudos(matriz_colectivo, matriz_recaudo)

                continuar = input("Desea continuar agregando recaudos a otra linea/interno? Si/No: ")
                    
                continuar = continuar.upper()
                    
                if continuar == "NO":
                    break
                
            bandera_validar = True

        case "B":

            if bandera_validar == True :
                print("Lineas de colectivos:") 
                mostrar_matriz(matriz_colectivo)
                print("Recaudos:") 
                mostrar_matriz(matriz_recaudo)
            else:
                print("Ingrese opcion A")
            
        case "C":

            if bandera_validar == True :
                
                suma_filas(matriz_recaudo)
                
                
            else:
                print("Ingrese opcion A")
            
        case "D":

            if bandera_validar == True :
                
                mostrar_recaudacion_coche(matriz_recaudo, matriz_colectivo)

            else:
                print("Ingrese opcion A")
            
        case "E":

            if bandera_validar == True :
                
                mostrar_recaudacion_total(matriz_recaudo, matriz_colectivo)
            else:
                print("Ingrese opcion A")

        case "F":
            
            break
                    
                    
        case _:
            error = input("Error: ingrese una opción válida: ")
    