def stark_normalizar_datos(lista_personajes:list) -> bool:

    modificado = False

    for i in range(len(lista_personajes)):
        

        if type(lista_personajes[i]["fuerza"]) != int:

            fuerza = int(lista_personajes[i]["fuerza"])
            
            modificado = True

            lista_personajes[i]["fuerza"] = fuerza

        

        if type(lista_personajes[i]["altura"]) != float:
            
            altura = float(lista_personajes[i]["altura"])
            
            modificado = True

            lista_personajes[i]["altura"] = altura
            


        if type(lista_personajes[i]["peso"]) != float:

            peso = float(lista_personajes[i]["peso"])
            
            modificado = True

            lista_personajes[i]["peso"] = peso

       
    return modificado
#----------------------------------------------------------------------------------------------------------------------------------------
def obtener_datos(heroes:dict, key:str) -> str:

    datos = (heroes[key])
    
    if heroes[key] == "":

        datos = False

    return datos
#----------------------------------------------------------------------------------------------------------------------------------------
def obtener_nombre(diccionario:dict) ->str:

    nombre = False
 
    nombre = obtener_datos(diccionario, "nombre")

    nombre = f"Nombre: {nombre}"

    return nombre
#----------------------------------------------------------------------------------------------------------------------------------------
def obtener_nombre_y_dato(diccionario: dict, key:str) -> str:

    datos = obtener_datos(diccionario, key)

    nombre = obtener_nombre(diccionario)

    return datos, nombre

# print(obtener_nombre_y_dato(lista_personajes[7], "fuerza"))
#----------------------------------------------------------------------------------------------------------------------------------------
def obtener_maximo(lista_heroes: list, key: str) -> int|bool|float :

    bandera = False
    
    for i in range(len(lista_heroes)):

        datos = obtener_datos(lista_heroes[i], key)

        if type(datos) == int or float:

            if bandera == False:
                
                datos_maximo = datos
                bandera = True
                
            else:
                if datos > datos_maximo:

                    datos_maximo = datos

        else:

            datos_maximo = False
            
            break

    return datos_maximo
    
# print(obtener_maximo(lista_personajes, "fuerza"))
#----------------------------------------------------------------------------------------------------------------------------------------
def obtener_minimo(lista_heroes: list, key: str):
    bandera = False
    
    for i in range(len(lista_heroes)):

        datos = obtener_datos(lista_heroes[i], key)

        if type(datos) == int or float:

            if bandera == False:
                
                datos_minimo = datos
                bandera = True
                
            else:
                if datos < datos_minimo:

                    datos_minimo = datos

        else:

            datos_minimo = False
            
            break
        
    return datos_minimo

# print(obtener_minimo(lista_personajes, "altura"))
#----------------------------------------------------------------------------------------------------------------------------------------
def obtener_dato_cantidad(lista_heroes: list, dato:float | int | str, key:str) -> list:
        lista_vacia = []
        
        for i in range(len(lista_heroes)):

            dato_obtenido = obtener_datos(lista_heroes[i], key)

            if dato_obtenido == dato:

                datos = lista_heroes[i]
                
                lista_vacia.append(datos)


        return lista_vacia

# mayor_altura = obtener_maximo(lista_personajes, "fuerza")
# lista_max_fuerza = obtener_dato_cantidad(lista_personajes, mayor_altura, "fuerza")
# print(lista_max_fuerza)
#----------------------------------------------------------------------------------------------------------------------------------------
def stark_imprimir_heroes(lista_heroes:list) -> bool|list:
    bandera = False

    if lista_heroes != []:

        for i in range(len(lista_heroes)):

            print(lista_heroes[i])

    return bandera

# mas_pesado = obtener_maximo(lista_personajes, "fuerza")
# lista_mas_pesados = obtener_dato_cantidad(lista_personajes,mas_pesado ,"fuerza") 
# stark_imprimir_heroes(lista_mas_pesados)
#----------------------------------------------------------------------------------------------------------------------------------------
def sumar_dato_heroe(lista_heroes:list, key:str) -> int | bool | float:

    suma = 0

    for i in range(len(lista_heroes)):

        if type(lista_heroes[i]) == dict and lista_heroes !=[]:
        
            suma += lista_heroes[i][key]

        else:
            
            suma = False
            break
        

    return suma

# print(sumar_dato_heroe(lista_personajes, "altura"))
#----------------------------------------------------------------------------------------------------------------------------------------
def dividir(dividendo: int | float, divisor:int | float) -> float:
    
    resultado = False

    if divisor != 0:

        resultado = dividendo/divisor

    return resultado
#----------------------------------------------------------------------------------------------------------------------------------------
def calcular_promedio(lista_heroes:list, key:str) -> float:

    suma = sumar_dato_heroe(lista_heroes, key)

    resultado = dividir(suma, len(lista_heroes))

    return resultado
# print(calcular_promedio(lista_personajes, "fuerza"))
#----------------------------------------------------------------------------------------------------------------------------------------
def mostrar_promedio_dato(lista: list[dict], key:str):

    retorno = False
    if lista != []:
        for i in range(len(lista)):
            tipo_dato = type(lista[i].get(key))
            if tipo_dato == int or tipo_dato == float:
                retorno = True

    return retorno

# mostrar_promedio_dato(lista_personajes, "fuerza")
 #----------------------------------------------------------------------------------------------------------------------------------------           
def imprimir_menu() -> None:

    print("""

    1. Normalizar los datos
    2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
    3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
    6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
    7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
    8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    10. Listar todos los superhéroes agrupados por color de ojos.
    11. Listar todos los superhéroes agrupados por tipo de inteligencia.
    """)
#----------------------------------------------------------------------------------------------------------------------------------------       
def validar_entero(string:str):

    if string.isdigit():
            
        retorno = True
        
    else:
            
        retorno = False
            

    return retorno
#----------------------------------------------------------------------------------------------------------------------------------------
def stark_menu_principal() -> bool | int:

    imprimir_menu()

    retorno = input("Ingrese una opcion: ")

    if validar_entero(retorno) == True:
        
        retorno = int(retorno)
    
    else: 

        retorno = False
    
    return retorno
#----------------------------------------------------------------------------------------------------------------------------------------