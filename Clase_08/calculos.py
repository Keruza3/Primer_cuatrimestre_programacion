def suma_filas(matriz:list) -> None:

    for i in range(len(matriz)):
        print(f"Fila numero {i + 1}")
        suma_filas = 0
        
        for j in range(len(matriz[i])):
            suma_filas += matriz[i][j]

        print(f"Resulado : {suma_filas}")

        