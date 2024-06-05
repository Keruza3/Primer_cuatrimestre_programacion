from functools import *
from funciones_validar import *
import json


#------------------------------------------------------------------------------------------------- 
def mostrar_menu(clave:str) -> None:

    match clave:
        case "principal":
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

        case "menu_modificar":
            print(
            """
            A- Nombre
            B- Apellido
            C- Puesto
            D- Salario
            E- Salir"
            """)
        
        case "ordenar":

            print("""
                A- Nombre
                B- Apellido
                C- Salario
                D- Salir
                """)
            
        case "sub-menu ordenar":

            print("""
                1) Ascendente
                2) Descendente 
                """)
            
        case "menu-mostrar":

            print("""
                    A) Empleados con determinado puesto.
                    B) Empleados con determinado salario.
                    C) Empleados con determinado apellido.
                    """)
#------------------------------------------------------------------------------------------------- 
def json_csv() -> list[dict]:
    while True:
    
        opcion = input("Quiere leer los datos en un archivo tipo (1)CSV o (2)JSON: ")
        retorno = ""

        if opcion == "1":
            
            lista_empleados = cargar_personas_csv("Clase_15/AMB_ARCHIVOS/empleados.csv")
            break

        else:
            if opcion == "2":
                with open("Clase_15/AMB_ARCHIVOS/empleados.json", "r") as archivo:
                    
                    data = json.load(archivo)
                    lista_empleados = data["empleados"]
                break
                
        if retorno == "":
            print(f"\n (Tiene que ingresar un numero para elegir la opcion)\n")

    return lista_empleados
#------------------------------------------------------------------------------------------------- 
def eliminar() -> str:

    retorno = ""

    ids = input("Ingrese el id del empleado que quiere buscar: ")
    
    lista_empleados = cargar_personas_csv("Clase_15/AMB_ARCHIVOS/empleados.csv")

    for empleados in lista_empleados:

        if empleados["ID"] == ids:

            lista_empleados.remove(empleados)
            retorno = "Empleado eliminado correctamente"    
            actualizar_datos(lista_empleados, "empleados")
            break

    return retorno
#------------------------------------------------------------------------------------------------- 
def calcular_salario_promedio() -> None:
    
    lista_empleados = cargar_personas_csv("Clase_15/AMB_ARCHIVOS/empleados.csv")
    salario = reduce(lambda total, salario: total + salario["salario"], lista_empleados, 0)

    salario / len(lista_empleados) -1

    mensaje = f"El salario promedio entre todos los empleados es de {salario}"

    return mensaje
#------------------------------------------------------------------------------------------------- 
def crear_empleado(ids:int, lista_empleados:list) -> dict:

    retorno = ""
    
    nombre = validar_nombre_apellido("Nombre")
    apellido = validar_nombre_apellido("Apellido")
    puesto = validar_puesto()
    salario =  validar_salario()
    
    diccionario = {
    "ID": ids,
    "Nombre":nombre,
    "Apellido":apellido,
    "Puesto":puesto,
    "Salario":salario}

    if lista_empleados ==[]:

        with open("Clase_15/AMB_ARCHIVOS/empleados.json", "a") as archivo:
            lista_empleados.append(diccionario)
            data = {}
            data["empleados"] = lista_empleados
            json.dump(lista_empleados, archivo, indent=4, ensure_ascii=False)

    with open("Clase_15/AMB_ARCHIVOS/empleados.csv", "r") as archivo:

        archivo.seek(0)
        linea = archivo.readline()

    if linea == "":

        with open("Clase_15/AMB_ARCHIVOS/empleados.csv", "a") as archivo:
            
            archivo.write("Nombre,Apellido,puesto,salario,ids\n")

    with open("Clase_15/AMB_ARCHIVOS/empleados.csv", "a") as archivo:
        
        archivo.write(f"{nombre},{apellido},{puesto},{salario},{ids}\n")

    print(f"--Se ingreso a la empleado con el ID: {ids} en el sistema--")

    if retorno != "":

        actualizar_datos(lista_empleados, "empleados")
    
    else:
        retorno = "No se pudo eliminar al empleado"

    return retorno

#------------------------------------------------------------------------------------------------- 
def modificar(lista_empleados: list[dict]) -> None:
    
    ids = input("Ingrese el ID del empleado que busca: ")

    for i in range(len(lista_empleados)):

        empleado = lista_empleados[i]["ID"] 
         
        if empleado == ids:

            retorno = ""

            while True:

                mostrar_menu("menu_modificar")

                opcion = input("Ingrese una de las opciones: ").upper()
                
                match opcion:

                    case "A":

                        retorno += modificar_caso(lista_empleados[i], "nombre", retorno, validar_nombre_apellido("Nombre"))

                    case "B":
                        
                        retorno += modificar_caso(lista_empleados[i], "apellido", retorno, validar_nombre_apellido("Apellido"))

                    case "C":
                        
                        retorno += modificar_caso(lista_empleados[i], "puesto", retorno, validar_puesto())

                        
                    case "D":
                        
                        retorno += modificar_caso(lista_empleados[i], "salario", retorno, validar_salario())

                    case "E":
                        
                        if retorno == "":
                            print("""\n
                                    -----------------------------------
                                    ¡No se hicieron cambios!
                                    -----------------------------------
                                    \n""")

                        break
                    case _:
                        
                        print("##ERROR##")
            
            actualizar_datos(lista_empleados, "empleados")
            return retorno
#-------------------------------------------------------------------------------------------------         
def cargar_personas_csv(path:str)-> list[dict]:
    
    with open(path, 'r') as archivo:

        lineas = archivo.readlines()
      
    lista_personas = []

    for i in range(1, len(lineas)):

        datos = lineas[i].replace("\n", "")
        datos = datos.split(',')
        
        ids = datos[4]
        nombre = datos[0]
        apellido = datos[1]
        puesto = datos[2]
        salario = int(datos[3])
    
        persona =   { 
                    "ID": ids,
                    "nombre": nombre,
                    "apellido": apellido,
                    "puesto": puesto,
                    "salario": salario
                    }

        lista_personas.append(persona)
    
    return lista_personas
#-----------------------------------------------------------------------------------------------------
def imprimir_empleados(clave:str, lista_alternativa = []) -> None:
    
    lista_empleados = cargar_personas_csv("Clase_15/AMB_ARCHIVOS/empleados.csv")

    match clave:
        case "opcion 5":

            mostrar_menu("menu-mostrar")
            opcion = input("Ingrese de que forma quiere ordenar los empleados: ").upper()

            match opcion:

                case  "A":
                    puesto = validar_puesto()
                    lista = filter(lambda empleado : empleado["puesto"] == puesto, lista_empleados)

                case "B":
                    salario = validar_salario()
                    lista = filter(lambda empleado : empleado["salario"] == salario, lista_empleados)

                case "C":
                    apellido = validar_nombre_apellido("apellido")
                    lista = filter(lambda empleado : empleado["apellido"] == apellido, lista_empleados)

            for empleados in lista:
                mensaje =   f"""
                            ********************************************************************************************
                                Nombre: {empleados["nombre"]}
                                Apellido: {empleados["apellido"]}	
                                Puesto: {empleados["puesto"]}	
                                Salario: {empleados["salario"]}	
                            ********************************************************************************************
                            """
                
                print(mensaje)

        case "opcion 6":
            lista_gerentes = list(filter(lambda empleados : empleados["puesto"] == "Gerente", lista_empleados))

            if lista_gerentes != []:
                for empleados in lista_gerentes:

                    mensaje =   f"""
                                ********************************************************************************************
                                    Nombre: {empleados["nombre"]}
                                    Apellido: {empleados["apellido"]}	
                                    Puesto: {empleados["puesto"]}	
                                    Salario: {empleados["salario"]}	
                                ********************************************************************************************
                                """
                    print(mensaje)

                    actualizar_datos(lista_gerentes, "gerentes")
            else:
                print("Empleados en la lista")
        case "opcion 7":
            lista_analistas = filter(lambda empleados: empleados["puesto"] == "Analista" and empleados["salario"] >= 500000, lista_empleados)

            if lista_analistas != []:
                for empleados in lista_analistas:
                    mensaje =   f"""
                                ********************************************************************************************
                                    Nombre: {empleados["nombre"]}
                                    Apellido: {empleados["apellido"]}	
                                    Puesto: {empleados["puesto"]}	
                                    Salario: {empleados["salario"]}	
                                ********************************************************************************************
                                """
                    print(mensaje)
        case "opcion 9":
            for empleados in lista_alternativa:
                mensaje =   f"""
                                ********************************************************************************************
                                    Nombre: {empleados["nombre"]}
                                    Apellido: {empleados["apellido"]}	
                                    Puesto: {empleados["puesto"]}	
                                    Salario: {empleados["salario"]}	
                                ********************************************************************************************
                                """
                print(mensaje)
#-----------------------------------------------------------------------------------------------------
def actualizar_datos(lista_actualizada:list[dict], direccion:str) -> None:

    path_csv = f"Clase_15/AMB_ARCHIVOS/{direccion}.csv"
    path_json = f"Clase_15/AMB_ARCHIVOS/{direccion}.json"

    lista_vacia = []

    with open(path_csv, "w") as archivo:
        
        archivo.write("Nombre,Apellido,puesto,salario,ids\n")

    for i in range(len(lista_actualizada)):
        
        ids = lista_actualizada[i]["ID"]
        nombre = lista_actualizada[i]["nombre"]
        apellido = lista_actualizada[i]["apellido"]
        puesto = lista_actualizada[i]["puesto"]
        salario = lista_actualizada[i]["salario"]
    
        persona =   { 
                    "ID": ids,
                    "nombre": nombre,
                    "apellido": apellido,
                    "puesto": puesto,
                    "salario": salario
                    }
        
        lista_vacia.append(persona)

        with open(path_csv, "a") as archivo:
            
            archivo.write(f"{nombre},{apellido},{puesto},{salario},{ids}\n")
    
    with open(path_json, "w") as archivo:

            json.dump(lista_vacia, archivo, indent = 4, ensure_ascii = False)
#-----------------------------------------------------------------------------------------------------
def ordenar_empleados() -> list[dict]:
    lista_empleados = cargar_personas_csv("Clase_15/AMB_ARCHIVOS/empleados.csv")

    mostrar_menu("ordenar")
    opcion = input("Ingrese como quiere ordenar a los empleados: ").upper()

    while opcion != "A" and opcion !="B" and opcion !="C" and opcion != "D":
        opcion = input("Ingrese como quiere ordenar a los empleados: ").upper()

    mostrar_menu("sub-menu ordenar")

    opcion_2 = input("Ingrese como quiere ordenar el menu: ")

    while opcion_2 != "1" and opcion_2 != "2":
        opcion_2 = input("Ingrese como quiere ordenar el menu: ")

    match opcion:
        case "A":
            if opcion_2 == "1":
                bubble_sort("ascendente", "nombre", lista_empleados)

            else:
                if opcion_2 == "2":
                    bubble_sort("descendente", "nombre", lista_empleados)

        case "B":
            if opcion_2 == "1":
                bubble_sort("ascendente", "apellido", lista_empleados)

            else:
                if opcion_2 == "2":
                    bubble_sort("descendente", "apellido", lista_empleados)
        
        case "C":
            if opcion_2 == "1":
                bubble_sort("ascendente", "salario", lista_empleados)

            else:
                if opcion_2 == "2":
                    bubble_sort("descendente", "salario", lista_empleados)
        
        case "D":
            pass 
#-----------------------------------------------------------------------------------------------------
def bubble_sort(orden:str , criterio:str, lista_empleados:list[dict]):

    for j in range(len(lista_empleados)):
        cambio = False

        for i in range(len(lista_empleados)-1 -j): 
            if orden == "ascendente":

                if lista_empleados[i][criterio] > lista_empleados[i+1][criterio]:
                    auxiliar=lista_empleados[i]
                    lista_empleados[i] = lista_empleados[i+1]
                    lista_empleados[i+1] = auxiliar
                    cambio = True
            else:
                
                if lista_empleados[i][criterio] < lista_empleados[i+1][criterio]:
                    auxiliar = lista_empleados[i]
                    lista_empleados[i] = lista_empleados[i+1]
                    lista_empleados[i+1] = auxiliar
                    cambio = True

        if cambio == False:
            
            break
    
    imprimir_empleados("opcion 9", lista_empleados)