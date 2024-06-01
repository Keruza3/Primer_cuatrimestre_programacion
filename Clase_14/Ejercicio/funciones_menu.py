from funciones_validar import *
from funciones_recursivas import *

lista_empleados = []
#------------------------------------------------------------------------------------------------- 
def mostrar_empleados(lista_empleados:list[dict]):

    for i in range(len(lista_empleados)):
            print(formatear_mensaje_empleados(lista_empleados[i]))

#------------------------------------------------------------------------------------------------- 
def formatear_mensaje_empleados(empleado:dict):
    mensaje = f"""
                ********************************************************************************************
                ID: {empleado['ID']}
                Nombre: {empleado['Nombre']}
                Apellido:{empleado['Apellido']}	
                Puesto: {empleado['Puesto']}
                Salario: {empleado['Salario']}
                ******************************************************************************************** 
                """
    return mensaje
#------------------------------------------------------------------------------------------------- 

def calcular_promedio(lista:list, clave:str):

    total_clave = sumar_salario_empleado(lista, clave)
    total_salario = len(lista)
    promedio = dividir(total_clave, total_salario)

    return promedio
#------------------------------------------------------------------------------------------------- 
def mostrar_gerente(lista_empleados:list):
    lista_gerentes = []

    for i in range(len(lista_empleados)):
        
        if lista_empleados[i]["Puesto"] == "Gerente":
            lista_gerentes.append(lista_empleados[i])
        
    mostrar_empleados(lista_gerentes)
#------------------------------------------------------------------------------------------------- 
def modificar(lista_empleados: list[dict]) -> None:
    
    ids = int(input("Ingrese el ID del empleado que busca: "))

    for i in range(len(lista_empleados)):

        retorno = ""
        
        if lista_empleados[i]["ID"] == ids:

            while True:

                mostrar_menu("menu_modificar")

                opcion = input("Ingrese una de las opciones: ").upper()
                
                match opcion:

                    case "A":

                        retorno += modificar_caso(lista_empleados[i], "Nombre", retorno, validar_nombre_apellido("Nombre"))

                    case "B":
                        
                        retorno += modificar_caso(lista_empleados[i], "Apellido", retorno, validar_nombre_apellido("Apellido"))

                    case "C":
                        
                        retorno += modificar_caso(lista_empleados[i], "Puesto", retorno, validar_puesto())

                        
                    case "D":
                        
                        retorno += (lista_empleados[i], "Salario", retorno, validar_salario())

                    case "E":
                        
                        
                        if retorno != "":
                            print(
    """\n
    -----------------------------------
    ¡Ya se guardaron los cambios! 
    -----------------------------------
    \n"""
    )
                        else:
                             print("""\n
    -----------------------------------
    ¡No se hicieron cambios!
    -----------------------------------
    \n""")

                        break
                    case _:
                        
                        print("##ERROR##")
                
        
        else:
            
            retorno = f"No se encontro a un empleado con el id: {ids}\n"

    
    return retorno

#------------------------------------------------------------------------------------------------- 
def eliminar(lista_empleados:list[dict]):     

    ids = int(input("ingrese el id del empleado que quiere eliminar: "))        

    retorno = ""

    for i in range(len(lista_empleados)):
        persona_lista = lista_empleados[i]

        if persona_lista["ID"] == ids:
            lista_empleados.pop(i)
            retorno = f"Se a eliminado correctamente a la persona con el ID {ids}"
            break
    
    if retorno == "":
        retorno = f"##ERROR## La persona con el ID {ids} no existe"
    
    return retorno
#------------------------------------------------------------------------------------------------- 
def agregar_empleado(empleado:dict, lista_empleados:list[dict]) -> list:

    retorno = ""

    if verificar_igualdad_id(empleado, lista_empleados) == True:
        retorno = "Este ID ya fui ingresado con anterioridad"
          
    else:
        lista_empleados.append(empleado)
        retorno = f"--Se ingreso a la empleado con el ID: {empleado['ID']}en el sistema--"

    return retorno
#------------------------------------------------------------------------------------------------- 
def crear_empleado(ids:int) -> dict:
    
    nombre = validar_nombre_apellido("Nombre")
    apellido = validar_nombre_apellido("Apellido")
    puesto = validar_puesto()
    salario =  validar_salario()

    diccionario = {
    "ID": ids,
    "Nombre":nombre,
    "Apellido":apellido,
    "Puesto":puesto,
    "Salario":salario
     }
    
    return diccionario
#-------------------------------------------------------------------------------------------------    