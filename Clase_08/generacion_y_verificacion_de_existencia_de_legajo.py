import random
from Package_Input.Input import get_int


def crear_legajos (matriz_vacia:list) -> list:

    legajo = random.randint(1, 1000)

    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):

            legajo += 1

            matriz_vacia[i][j] = legajo


    return matriz_vacia


def validar_legajo(matriz:list) -> bool:

    numero = get_int("Ingrese el numero de legajo: ", "ERROR. Reingrese el numero de legajo: " , 1, 1016, 3)

    for i in range(len(matriz)):
            for j in range(len(matriz[i])):

                if numero == matriz[i][j]:

                    return True
                
                else:

                    return False
                
