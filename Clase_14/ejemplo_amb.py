lista_personas = []

def crear_personas()->dict:

    nombre = input("Ingrese su nombre: ")

    apellido = input("Ingrese su apellido: ")

    edad = int(input("Ingrese su edad: "))

    dni = int(input("Ingrese a su dni: "))

    peronsa_nueva = {"nombre": nombre,
                     "apellido": apellido,
                     "edad": edad,
                     "dni": dni}
    
    return peronsa_nueva

def agregar_persona(persona:dict, lista_personas:list[dict])-> str:

    retorno = ""

    for i in range(lista_personas):

        persona_lista = lista_personas[i]

        if persona_lista["dni"] == persona["dni"]:
            retorno = "##ESTE##DNI##YA##FUE##INGRESADO##CON##ANTERIORIDAD##"
            break

    if retorno == "":
        lista_personas.append(persona)
        retorno = f"--Se ingreso a la persona con el DNI: {persona['dni']}en el sistema--"

    return retorno

def modificar_persona(dni:int, lista_personas:list[dict])-> str:

    retorno = ""
    bandera_existe = False

    for i in range(len(lista_personas)):
        persona = lista_personas [i]

        if persona['dni'] == dni:
            bandera_existe = True

            while True:
                print("A- Nombre\nB- Apellido\nC- Edad\nD- D.N.I\nE- Salir")
                opcion = input("Ingrese una de las opciones: ").upper()
                
                match opcion:

                    case 'A':
                        nombre = "Elija un nombre para cambiar: "
                        persona['nombre'] = nombre
                        retorno += "Se modifico el nombre.\n"

                    case 'B':
                        apellido = "Elija un apellido para cambiar: "
                        persona['apellido'] = apellido
                        retorno += "Se modifico el apellido.\n"

                    case 'C':
                        edad = "Elija un edad para cambiar: "
                        persona['edad'] = edad
                        retorno += "Se modifico el edad.\n"

                    case 'D':
                        dni = "Elija un dni para cambiar: "
                        persona['dni'] = dni
                        retorno += "Se modifico el dni.\n"

                    case 'E':
                        print('Todos los datos cambiados ya fueron modificados.')

                    case _:
                        print('##ERROR##')
                        break
            break

    if retorno == "":
        retorno = "No hubieron modificaciones."

    if bandera_existe == False:
        retorno = "No se encontro el dni / persona."

    return retorno

def eliminar(lista_personas:list[dict], dni:str)-> str:

    retorno = ""

    for i in range(lista_personas):
        persona_lista = lista_personas[i]

        if persona_lista["dni"] == dni:
            lista_personas = persona_lista.pop(i)
            retorno = f"Se a eliminado correctamente a la persona con el dni {dni}"
            break
    
    if retorno == "":
        retorno = f"##ERROR## La persona con el dni {dni} no existe"

    return retorno

def mostrar_personas(lista_personas:list[dict])-> None:

    print("--DICCIONARIO--")

    for i in range(len(lista_personas)):
        persona = lista_personas[i]
        print(f"Trabajador numero {i + 1}")
        print(persona)
