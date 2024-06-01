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