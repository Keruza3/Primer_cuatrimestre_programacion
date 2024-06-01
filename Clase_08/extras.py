def mostrar_matriz(matriz:list)-> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]: 4}', end='')

        print("")
