from funciones_validar import *
import json

#------------------------------------------------------------------------------------------------- 
def mostrar_menu(clave:str) -> None:

    if clave == "principal":

        print(
        """
        1. Leer desde CSV / JSON
        2. Dar de alta.
        3. Modificar.
        4. Eliminar.
        5. Mostrar todos.
        6. Mostrar gerentes.
        7. Mostrar Analistas con sueldo mayor a $500000.
        8. Calcular salario promedio.
        9. Ordenar empleados.
        10. Salir.
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

#-----------------------------------------------------------------------------------------------------
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

    with open("Clase_15/ejercicio_abm_archivos/empleados.json", "a") as archivo:

        json.dump(diccionario, archivo, indent=4, ensure_ascii=False)

    with open("Clase_15/ejercicio_abm_archivos/empleados.csv", "r") as archivo:

        archivo.seek(0)
        linea = archivo.readline()

    if linea == "":

        with open("Clase_15/ejercicio_abm_archivos/empleados.csv", "a") as archivo:
            
            archivo.write("Nombre,Apellido,puesto,salario,ids,\n")


    with open("Clase_15/ejercicio_abm_archivos/empleados.csv", "a") as archivo:
        
        archivo.write(f"{nombre},{apellido},{puesto},{salario},{ids},\n")

    print(f"--Se ingreso a la empleado con el ID: {ids} en el sistema--")

def eliminar_empleado() -> str:

    # with open("Clase_15\ejercicio_abm_archivos\empleados.json", "r") as archivo:
        
    #     empleados = json.load(archivo)

    # empleados = list(empleados)

    # for empleado in range(len(empleados)):

    #     if empleado["ID"] == ids_buscar:

    #         print("hola")

    ids_buscar = input("Ingrese el id del empleado que eliminar: ")

    with open("Clase_15/ejercicio_abm_archivos/empleados.csv", "r") as archivo:

        empleados = archivo.read()

    empleados = empleados.replace("\n", "")
    empleados = empleados.split(",")
    

    for i in range(4, len(empleados), 5):

        if ids_buscar == empleados[i]:

            print("Empleado encontrado")
            
            while True:

                confirmacion = input(f"¿esta seguro que quiere eliminar al empleado con el id {empleados[i]}? s/n: ").lower()

                if confirmacion == "s":
                    
                    for j in range(i - 4 , i + 1):
                        
                        datos_temporales = empleados[i - 4]

                        empleados.remove(datos_temporales)
                    
                    reescribir_archivos(empleados)

                    retorno = "Empleado a sido eliminado correctamente."

                else:
                    if confirmacion == "n":

                        break

                    else:
                        confirmacion = input("Ingrese s si lo quiere elinimar en el caso contrario ingrese n")

                return retorno
                    
def reescribir_archivos(lista_nueva_csv:list):
    pass
#     contador = 0

#     with open("Clase_15\ejercicio_abm_archivos\empleados.csv", "w") as archivo:
        
#         for i in range(len(lista_nueva_csv)):

#             contador +=1

#             if contador % 5 == 0:

#                 archivo.write(f"{lista_nueva_csv[i]},\n")
#                 contador = 0

#             else:
                
#                 archivo.writelines(f"{lista_nueva_csv[i]},")


def aplicacion_principal() -> None:

    bandera = False

    while True:

        mostrar_menu("principal")

        opcion = int(input("Ingrese una opcion: "))
        
        match opcion:
            
            case 1:

                archivo = json_csv()

                bandera = True
                
            case 2:

                if bandera == True:
                    
                    ids = controlar_ids()
                    crear_empleado(ids)

                else:
                    print("Primero debe leer desde un tipo de archivo")
            
            case 3:

                if bandera == True:
                    
                    
                    pass
                    
                else:
                    print("Primero debe leer desde un tipo de archivo")
            case 4:

                if bandera == True:
                    
                    print(eliminar_empleado())
                else:
                    
                    print("Primero debe leer desde un tipo de archivo")
            case 5:

                if bandera == True:
                    # mostrar_gerente(lista_empleados)
                    pass
                else:
                    print("Primero debe leer desde un tipo de archivo")
            case 6:
                if bandera == True:
                    # print(calcular_promedio(lista_empleados, "Salario") )
                    pass           
                else:
                    print("Primero debe leer desde un tipo de archivo")
                    
            case 7:
                print("""\n
                    -----------------------------------
                    !Gracias por utilizar el programa!
                    -----------------------------------
                    \n""")
                break

           
                         
aplicacion_principal()