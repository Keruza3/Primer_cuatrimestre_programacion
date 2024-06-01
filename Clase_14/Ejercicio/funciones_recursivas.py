from funciones_validar import *

#------------------------------------------------------------------------------------------------- 
def modificar_caso(diccionario_empleado:dict, clave:str, retorno: str, funcion) -> str:
    
    diccionario_empleado[clave] = funcion
    retorno = f"Se modifico el {clave} correctamente.\n"
    
    return retorno
#------------------------------------------------------------------------------------------------- 
def mostrar_menu(clave:str) -> None:

    if clave == "principal":

        print(
        """
        1. Dar de alta.
        2. Modificar.
        3. Eliminar.
        4. Mostrar todos.
        5. Mostrar gerentes.
        6. Calcular salario promedio.
        7. Salir.
        """)
    else:
        if clave == "menu_modificar":
            
            print(
            """
            A- Nombre
            B- Apellido
            C- Puesto
            D- Salario
            E- Salir"
            """)
#-------------------------------------------------------------------------------------------------      
def sumar_salario_empleado(lista_empleados:list, clave:str)-> int | float:

    suma_clave = 0

    for i in range(len(lista_empleados)):

        dato = lista_empleados[i]

        if type(dato) == dict and lista_empleados[i] != {}:
            suma_clave += int(dato[clave])

    return suma_clave
#-------------------------------------------------------------------------------------------------    
def dividir(dividendo: int|float, divisor: int|float)-> bool | int | float:
    retorno = False

    if divisor != 0:
        retorno = dividendo / divisor

    return retorno
