def validar_linea(matriz:list, linea:int) -> bool:
    for i in range(len(matriz)):
        if matriz[i][0] == linea:

            return True
        
    print("________________________________")
    return False
    

def validar_interno(matriz:list, interno:int) -> bool:

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == interno:

                return True
        
    print("________________________________")
    return False
