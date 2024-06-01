from Package_Input.Input import get_int

def mostrar_matriz(matriz:list)-> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]: 4}', end='')

        print("")

#Desafio A - Multiplicacion entre matrices


filas_a = get_int("Ingrese la cantidad de filas que quiera tener en su matriz a: ", "Numero invalido", 1, 100, 3 )
columnas_a = get_int("Ingrese la cantidad de columnas que quiera tener en su matriz a: ", "Numero invalido", 1, 100, 3 )

matriz_a_vacia = [[0]* columnas_a for _ in range(filas_a)]

filas_b = get_int("Ingrese la cantidad de filas que quiera tener en su matriz b: ", "Numero invalido", 1, 100, 3 )
columnas_b = get_int("Ingrese la cantidad de columnas que quiera tener en su matriz b: ", "Numero invalido", 1, 100, 3 )


matriz_b_vacia = [[0]* columnas_b for _ in range(filas_b)]


if  columnas_a == filas_b:
        
    matriz_resultado =[[0]* filas_a for _ in range(columnas_b)]
        
    for i in range(len(matriz_a_vacia)):
        for j in range(len(matriz_a_vacia[i])):

            matriz_a_vacia[i][j] = int(input(f'Ingrese un numero para la matriz A en la fila {i + 1} y en la columna {j + 1}: '))
            mostrar_matriz(matriz_a_vacia)


    for i in range(len(matriz_b_vacia)):
        for j in range(len(matriz_b_vacia[i])):

                matriz_b_vacia[i][j] = int(input(f'Ingrese un numero para la matriz B en la fila {i + 1} y en la columna {j + 1}: '))
                mostrar_matriz(matriz_b_vacia)

    for i in range(len(matriz_a_vacia)):
        for j in range(len(matriz_b_vacia[0])):
            for k in range(len(matriz_a_vacia)):
                    matriz_resultado[i][j] += matriz_a_vacia[i][k] * matriz_b_vacia[k][j]

        
    print("RESULTADO: ")
    mostrar_matriz(matriz_resultado)

else:
    print("Esta multipliacion no se puede realizar, intente nuevamente")







