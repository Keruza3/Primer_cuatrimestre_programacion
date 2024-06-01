from funciones_reutilizadas import *

def opcion_2(lista_personajes:list) -> None:

    # lista = obtener_dato_cantidad(lista_personajes, "NB", "genero")

    # stark_imprimir_heroes(lista)

    for i in range(len(lista_personajes)):
    
        if obtener_datos(lista_personajes[i], "genero") == "NB":

            print(obtener_nombre(lista_personajes[i]))
#----------------------------------------------------------------------------------------------------------------------------------------
def opcion_3_4_5_6(lista_personajes:list, genero:str, atributo:str) -> None:

    # Recorrer la lista y determinar cuál es el superhéroe más alto de género M

    lista_f = obtener_dato_cantidad(lista_personajes, genero, "genero")

    maximo_f = obtener_maximo(lista_f, atributo)

    final = obtener_dato_cantidad(lista_f, maximo_f, atributo)

    stark_imprimir_heroes(final)
#----------------------------------------------------------------------------------------------------------------------------------------

def opcion_7(lista_personajes:list) -> None:
    #Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB

    lista = obtener_dato_cantidad(lista_personajes, "NB", "genero")

    print(calcular_promedio(lista, "fuerza"))
#----------------------------------------------------------------------------------------------------------------------------------------
def opcion_8_9(lista_personajes:list, clave:str) -> None:
    #usar un metodo para no agregar los repetidos

    lista_ojos = set()

    for i in range(len(lista_personajes)):

        if type(obtener_datos(lista_personajes[i], clave)) != bool:

            lista_ojos.add(obtener_datos(lista_personajes[i], clave))

    lista_ojos = list(lista_ojos)

    lista_clone = []

    for i in range(len(lista_ojos)):

        bandera_color_ojos = True

        for j in range(len(lista_personajes)):
            
            validar = obtener_datos(lista_personajes[j], clave)

            if validar != False:

                if obtener_datos(lista_personajes[j], clave).capitalize() == lista_ojos[i]:

                    if bandera_color_ojos == False:

                        contador_color += 1

                    else:
                        contador_color = 1
                        bandera_color_ojos = False

        lista_clone.append(contador_color)

    for k in range(len(lista_clone)):

        print(f"En el color {lista_ojos[k]} se encontro: {lista_clone[k]}")


def opcion_10_11(lista_personajes:list, clave:str) -> None:

    lista_ojos = set()

    for i in range(len(lista_personajes)):

        lista_ojos.add(obtener_datos(lista_personajes[i], clave))

    lista_ojos = list(lista_ojos)

    for i in range(len(lista_ojos)):
        print(f"---{clave}: {lista_ojos[i]}---")

        for j in range(len(lista_personajes)):

            if obtener_datos(lista_personajes[j], clave) == lista_ojos[i]:
                print(lista_personajes[j]["nombre"])