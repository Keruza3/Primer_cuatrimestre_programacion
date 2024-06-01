from Package_Input.Input import get_int


def mostrar_matriz(matriz:list)-> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]: 4}', end='')

        print('')




#Desafio B - Cuadrado magico

filas_cuadrado = get_int('Ingrese la cantidad de filas para crear la matriz: ', 'Error, ingrese una cantidad de filas valida: ', 1, 10, 3)

columnas_cuadrado = get_int('Ingrese la cantidad de columnas para crear la matriz: ', 'Error, ingrese una cantidad de columnas valida: ', 1, 10, 3)


if filas_cuadrado == columnas_cuadrado:
    cuadrado_magico = [[0]*columnas_cuadrado for _ in range(filas_cuadrado)] 

    #----Recorre la matriz y guarda en los respectivos lugares de la matriz, el numero ingresado por el usuario----
    for i in range(len(cuadrado_magico)):
        for j in range(len(cuadrado_magico[i])):
            cuadrado_magico[i][j] = int(input(f'Ingrese un numero para la fila {i+1} y la columna {j+1}: '))
            mostrar_matriz(cuadrado_magico)

    
    #----SUMA DE FILAS----
    for i in range(len(cuadrado_magico)):
        suma_filas = 0
        for j in range(len(cuadrado_magico[i])):
            suma_filas += cuadrado_magico[i][j]


    #----SUMA DE COLUMNAS----
    for j in range(len(cuadrado_magico[0])):
        suma_columnas = 0
        for i in range(len(cuadrado_magico)):
            suma_columnas += cuadrado_magico[i][j]

    
    #----SUMA DIAGONAL PRINCIPAL----
    suma_diagonal_principal = 0
    for i in range(len(cuadrado_magico)):
        suma_diagonal_principal += cuadrado_magico[i][i]
        
        

    #----SUMA DIAGONAL MENOR----
    suma_diagonal_menor = 0
    fila = len(cuadrado_magico) -1
    for i in range(len(cuadrado_magico)):
        suma_diagonal_menor += cuadrado_magico[fila][i]
        fila += -1

            
    # print(suma_diagonal_principal)
    # print(suma_diagonal_menor)


    formula = filas_cuadrado*(filas_cuadrado**2 + 1)/2 
    "Esta formula funciona unicamente con matrices de 3x3 de un solo digito o 4x4 de uno/dos digitos"


    if suma_filas and suma_columnas and suma_diagonal_principal and suma_diagonal_menor == formula:

        print('Esta matriz es un cuadrado magico')
    
    else:
        print('Esta matriz no es un cuadrado magico')



else:
    print('No se puede realizar la matriz, ya que no cumple la condicion para ser cuadrada')
