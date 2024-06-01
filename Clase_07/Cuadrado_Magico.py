from Package_Input.Input import get_int


def mostrar_matriz(matriz:list)-> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]: 4}', end='')

        print('')

# cuadrado_magico = [[8,1,6],
#                    [3,5,7],
#                    [4,9,2]]


filas = get_int("Ingrese la cantidad de filas que quiera tener en su matriz: ", "Numero invalido", -1000, 10000, 3 )
columnas = get_int("Ingrese la cantidad de columnas que quiera tener en su matriz: ", "Numero invalido", -1000, 10000, 3 )

matriz = [[0]* columnas for _ in range(filas)]


if filas == columnas:

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            matriz[i][j] = int(input(f"Ingrese un numero para la matriz A en la fila {i+1} y en la columna {j+1}: "))
            mostrar_matriz(matriz)
    
    def suma_filas(matriz:list) -> int:

        suma_total = 0
            
        for i in range(len(matriz)):
            
            suma = 0
            
            for j in range(len(matriz[i])):
            
                suma += matriz[i][j]

                suma_total += matriz[i][j]
            
            return suma_total


    def suma_diagonales_principal(matriz:list) -> int:

        
        for i in range(len(matriz)):
            
            suma = 0
            
            for j in range(len(matriz[i])):
            
                suma += matriz[i][i]
                
            return suma
    

    def suma_diagonales_menor(matriz:list) -> int:

        
        for i in range(len(matriz)):
            
            suma = 0
            fila = filas - 1
            
            for j in range(len(matriz[i])):
            
                suma += matriz[fila][j]

                fila += -1
        
            return suma


    def suma_columnas(matriz:list) -> int:

        suma_total = 0
            
        for i in range(len(matriz)):
            
            for j in range(len(matriz[i])):

                suma_total += matriz[j][i]
            
            return suma_total


    matriz_final = filas * (filas ** 2 + 1)/2 #esta formula funciona unicamente para 3x3 de un digito y 4x4 de uno/dos digitos
    matriz_final = int(matriz_final)



    sum_filas = suma_filas(matriz) 
    sum_filas = sum_filas / filas



    sum_columnas =  suma_columnas(matriz)
    sum_filas = sum_columnas / filas




    if matriz_final == suma_diagonales_menor(matriz) and suma_diagonales_principal(matriz) and  sum_filas and sum_columnas:
        
        print("Esta matriz es un cuadrado magico")


    else:
        
        print("Esta matriz no es un cuadrado magico")


else:
    print(f"Error la cantidad de filas {filas} no coinciden con las columnas {columnas} intente nuevamente")