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
def crear_empleado(ids:int, clave:str) -> dict:
    
    nombre = validar_nombre_apellido("Nombre")
    apellido = validar_nombre_apellido("Apellido")
    puesto = validar_puesto()
    salario =  validar_salario()
    
    if clave == "JSON":

        diccionario = {
            "ID": ids,
            "Nombre":nombre,
            "Apellido":apellido,
            "Puesto":puesto,
            "Salario":salario
            }

        with open("Clase_15\ejercicio_abm_archivos\empleados.json", "a") as archivo:

            json.dump(diccionario, archivo, indent=4, ensure_ascii=False)

    else:

        with open("Clase_15\ejercicio_abm_archivos\empleados.csv", "r") as archivo:

            linea = archivo.readline()

        if linea == "":

            with open("Clase_15\ejercicio_abm_archivos\empleados.csv", "a") as archivo:
                
                archivo.write("Nombre, Apellido, Edad, salario, ids \n")


        with open("Clase_15\ejercicio_abm_archivos\empleados.csv", "a") as archivo:
            
            archivo.write(f"{nombre}, {apellido}, {puesto}, {salario}, {ids} \n")

        

    print(f"--Se ingreso a la empleado con el ID: {ids} en el sistema--")

def aplicacion_principal() -> None:

    bandera = False

    bandera_crear = False

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
                    crear_empleado(ids, archivo)

                    
                else:
                    print("debe primero dar de alta una persona")
            
            case 3:

                if bandera == True:
                    
                    # eliminar(lista_empleados)
                    pass
                    
                else:
                    print("debe primero dar de alta una persona")
            case 4:

                if bandera == True:
                    # mostrar_empleados(lista_empleados)
                    pass
                else:
                    print("debe primero dar de alta una persona")
            case 5:

                if bandera == True:
                    # mostrar_gerente(lista_empleados)
                    pass
                else:
                    print("debe primero dar de alta una persona")
            case 6:
                if bandera == True:
                    # print(calcular_promedio(lista_empleados, "Salario") )
                    pass           
                else:
                    print("debe primero dar de alta una persona")
                    
            case 7:
                print("""\n
                    -----------------------------------
                    !Gracias por utilizar el programa!
                    -----------------------------------
                    \n""")
                break

            case _: 
                print("##ERROR##")
                         
            
aplicacion_principal()