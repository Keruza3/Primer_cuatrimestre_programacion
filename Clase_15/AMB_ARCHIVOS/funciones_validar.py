def validar_puesto():

    lista_puestos = ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]
    puesto = input ("Ingrese el puesto (Gerente|Supervisor|Analista|Encargado|Asistente): ").capitalize()

    while True:
        for i in range(len(lista_puestos)):
            if puesto == lista_puestos[i]:

                retorno = puesto.capitalize()
                return retorno  
            
        retorno = print("Verifique que el campo ingresado sea un puesto valido.")
        puesto = input (f"Ingrese un puesto valido puesto: ").capitalize()
#-------------------------------------------------------------------------------------------------    
def validar_nombre_apellido(clave:str) -> str:

    identificacion = input (f"Ingrese el {clave}: ")
    longitud = len(identificacion)
    validar_letras = identificacion.isalpha()

    while True:
        if validar_letras == False or longitud > 15:

            print("Verifique que el campo ingresado no tenga mas de 15 caracteres y sean todos alfabeticos.")

            identificacion = input (f"Ingrese el {clave}: ")
            validar_letras = identificacion.isalpha()

        else:

            return identificacion  
#-------------------------------------------------------------------------------------------------   
def validar_salario()-> int:

    salario = input("Ingrese el salario del empleado: ")
    minimo = 234315

    while salario.isnumeric() != True or int(salario) < minimo:
        salario = input("Salario inválido. Ingrese nuevamente el salario del empleado (mayor a $234315): ")

    return int(salario)
#------------------------------------------------------------------------------------------------- 
def verificar_igualdad_id(clave:int, lista:list) -> bool:

    retorno = False

    for i in range(len(lista)):

        indice_lista = lista[i]

        if indice_lista["ID"] == clave:
            retorno = True
            break

    return retorno  
#------------------------------------------------------------------------------------------------- 
def controlar_ids(lista_empleados:list[dict]) -> int:

    bandera = False

    if lista_empleados != []:
        for i in range(1, len(lista_empleados)):

            id = int(lista_empleados[i]["ID"])

            if bandera == False:

                maximo = id

                bandera = True

            else:
                if id > maximo:

                    maximo = id

    return maximo + 1
#------------------------------------------------------------------------------------------------- 
def modificar_caso(diccionario_empleado:dict, clave:str, retorno: str, funcion) -> str:
    
    diccionario_empleado[clave] = funcion
    retorno = f"Se modifico el {clave} correctamente.\n"
    
    return retorno
#------------------------------------------------------------------------------------------------- 
def controlar_ids() -> int:
    with open("Clase_15/AMB_ARCHIVOS/ids.txt", "r") as archivo:

        ids = archivo.read()

    with open("Clase_15/AMB_ARCHIVOS/ids.txt", "a") as archivo:
        
        if ids == "":
            archivo.write("1")

    with open("Clase_15/AMB_ARCHIVOS/ids.txt", "r") as archivo: 

        ids = archivo.read()

    caracteres = len(ids)
    caracteres += 1
    
    with open("Clase_15/AMB_ARCHIVOS/ids.txt", "a") as archivo:
        
        caracteres = str(caracteres)
        archivo.write(caracteres)
    
    return caracteres