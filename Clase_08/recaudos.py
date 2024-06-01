from Package_Input.Input import get_int
from validaciones_de_líneas_y_coches import *


def almacenar_recaudos(matriz_colectivo:list, matriz_recaudo:list)-> None:

    linea = get_int("Ingrese su numero de linea: ", "Numero invalido, intente nuevamente: ", 1, 9999, 3)

    interno = get_int("Ingrese su numero de interno: ", "Numero invalido, intente nuevamente: ", 1, 9999, 3)
    
    if validar_linea(matriz_colectivo, linea) == True and validar_interno(matriz_colectivo, interno) == True:

        for i in range(len(matriz_colectivo)): 
            for j in range(1, len(matriz_colectivo[i])):
                if matriz_colectivo[i][j] == interno:
                    
                    columna = j - 1
                    matriz_recaudo[i][columna] = get_int("Ingrese el recaudo: ", "ERROR, Reingrese el reacudo: ", 1, 1000000, 3)
                    
        return matriz_recaudo
    

def mostrar_recaudacion_coche(matriz_recaudo:list, matriz_colectivo: list )-> None:

    for i in range(len(matriz_recaudo)):
        for j in range(len(matriz_recaudo[i])):
                    
            columna = j + 1
            coche = matriz_colectivo[i][columna]
            
        print(f"El coche {coche} tuvo una recaudacion de: {matriz_recaudo[i][j]}")

def mostrar_recaudacion_total(matriz_recaudo:list, matriz_colectivo: list )-> None:

    recaudacion_total = 0
    
    for i in range(len(matriz_recaudo)):
        for j in range(len(matriz_recaudo[i])):
                    
            recaudacion_total += matriz_recaudo [i][j]
    
    print(recaudacion_total)