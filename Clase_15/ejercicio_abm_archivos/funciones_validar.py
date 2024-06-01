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
def validar_nombre_apellido(clave:str):

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

    return salario
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
def json_csv() -> str:

    while True:
    
        opcion = input("Quiere guardar los datos en un archivo tipo (1)CSV o (2)JSON: ")

        retorno = ""

        if opcion == "1":
            retorno = "CSV"

        else:
            if opcion == "2":
                retorno = "JSON"

        if retorno == "":

            opcion = input("Quiere guardar los datos en un archivo tipo (1) CSV o (2) JSON (Tiene que ingresar un numero para elegir la opcion)")

        else:
            break

    return retorno
#------------------------------------------------------------------------------------------------- 
def controlar_ids() -> int:

    with open("Clase_15\ejercicio_abm_archivos\ids.txt", "r") as archivo:

        ids = archivo.read()


    with open("Clase_15\ejercicio_abm_archivos\ids.txt", "a") as archivo:
        
        if ids == "":
            archivo.write("0")

    with open("Clase_15\ejercicio_abm_archivos\ids.txt", "r") as archivo: 

        ids = archivo.read()

    caracteres = len(ids) - 1

    if caracteres == 0:
        caracteres = 1

    else:

        caracteres += 1
    
    with open("Clase_15\ejercicio_abm_archivos\ids.txt", "a") as archivo:
        
        caracteres = str(caracteres)
        archivo.write(caracteres)
    
    caracteres = int(caracteres)
    return caracteres