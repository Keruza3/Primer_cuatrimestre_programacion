#IDS
#ESPACIO MENUS
def mostrar_menus(clave:str) -> None:
    match clave:
        case "principal":
            print(
            """
            1. Dar de alta
            2. Modificar
            3. Eliminar
            4. Mostrar peliculas
            5. Ordenar peliculas
            6. Busqueda por titulo
            7. Calcular promedio
            8. Calcular porcentaje
            9. Salir
            """)
        
        case "modificar":
            print("""
            A- Titulo
            B- Genero
            C- Año de lanzamiento
            D- Duracion
            E- Atp
            F- Plataformas
            G- Salir
            """)

        case "mostrar peliculas":
            print("""
            A. Todas las peliculas
            B. De determinado genero
            C. De determinado año
            D. Todas las ATP
            E. Todas las no ATP
            F. De determinada plataforma
            G. Salir
            """)
        
        case "ordenar peliculas":
            print("""
            A. Titulo
            B. Genero
            C. Año de lanzamiento
            D. Duracion
            E. Salir
            """)
        case "sub menu ordenar":
            print("""
                1) Ascendente
                2) Descendente 
                """)
            
        case "calcular promedio":
            print("""
            A. Año de lanzamiento
            B. Duracion de peliculas
            C. Salir
            """)
        
        case "calcular porcentaje":
            print("""
            A. Porcentaje de genero
            B. Porcentaje por ATP
            C. Salir
            """)    

        case "porcentaje sub-menu":
            print("""
                    1. Imprimir solo un genero es especifico
                    2. Mostrar todos los generos
                    3. Salir
                  """)
#-------------------------------------------------------------------------------------------
def cargar_datos() -> list[dict]:
    #SACAR \N
    lista_peliculas = []

    with open("PARCIAL/peliculas.csv", "r", encoding="utf-8") as archivo:

        lista_temporal = archivo.readlines()

    for i in range(1, len(lista_temporal)):
        
        pelicula = lista_temporal[i]
        pelicula = pelicula.split(",")

        atp = pelicula[5]
        if atp == "Si":
            atp = True
        else:
            atp = False

        plataforma = pelicula[6]
        plataforma = plataforma.replace("\n", "")
        plataforma = plataforma.split("-")

        diccionario = {
        "id": int(pelicula[0]),
        "titulo":pelicula[1],
        "genero":pelicula[2],
        "año de lanzamiento":int(pelicula[3]),
        "duracion":int(pelicula[4]),
        "atp":atp,
        "plataforma":plataforma}

        lista_peliculas.append(diccionario)
    
    return lista_peliculas
#-------------------------------------------------------------------------------------------
def validar_atp() -> tuple:

    while True:
        bandera = False
        si_o_no = input("Ingrese si la pelicula ATP (Apto para todo publico) Si/No: ")

        if si_o_no != "":
            si_o_no = si_o_no.capitalize()

            match si_o_no:
                case "Si":
                    retorno = True
                    bandera = True

                case "No":
                    retorno = False
                    bandera = True
                
                case _:
                    print("Usted no ingreso lo pedido")

            if bandera == True:
                return si_o_no, retorno
        else:
            print("No puede dejar este campo vacio")
#-------------------------------------------------------------------------------------------
def controlar_ids(lista_peliculas:list[dict]) -> int:

    bandera = False
    for i in range(1, len(lista_peliculas)):
        
        if bandera == False:
            id_maxima = lista_peliculas[i]["id"]
            bandera = True
        else:
            id = lista_peliculas[i]["id"]
            if id > id_maxima:
                id_maxima_nueva = id

    with open("PARCIAL/ids.txt", "r") as archivo:
        id_anterior = archivo.read()

    with open("PARCIAL/ids.txt", "a") as archivo:
        
        if id_anterior == "":
            
            archivo.write("0")

    with open("PARCIAL/ids.txt", "r") as archivo:
        id_anterior = archivo.read()

    id_anterior = int(id_anterior)
    id_maxima_nueva = int(id_maxima_nueva)
    
    if id_maxima_nueva >= id_anterior:

        retorno = id_maxima_nueva + 1
    
    else: 
        retorno = id_anterior + 1

    with open("PARCIAL/ids.txt", "w") as archivo:
        retorno = str(retorno)
        archivo.write(retorno)
    
    retorno = int(retorno)

    return retorno
#-------------------------------------------------------------------------------------------
def validar_genero() -> str:
    lista_generos = ["Acción","Aventura", "Animación", "Biográfico", "Comedia", "Comedia romántica", "Comedia dramática",
                    "Crimen", "Documental", "Drama", "Fantasía", "Histórico", "Infantil", "Musical", "Misterio", "Policíaco", "Romance",
                    "Ciencia ficción", "Suspenso", "Terror", "Western", "Bélico", "Deportivo", "Noir", "Experimental", "Familiar",
                    "Superhéroes", "Espionaje", "Artes marciales", "Fantástico", "Catástrofe", "Melodrama", "Erótico", "Cine"
                    "independiente", "Zombies", "Vampiros", "Cyberpunk", "Steampunk", "Distopía", "Utopía", "Road Movie",
                    "Docuficción", "Mockumentary", "Gótico", "Slasher", "Adolescente", "Culto", "Maravilloso"]
    print("""
            ---------------------------------------------------------------------------------
            | Acción            | Aventura          | Adolescente      | Animación          |
            | Artes marciales   | Bélico            | Biográfico       | Catástrofe         |
            | Ciencia ficción   | Cine independiente| Comedia          | Comedia dramática  |
            | Comedia romántica | Crimen            | Culto            | Cyberpunk          |
            | Deporte           | Documental        | Docuficción      | Distopía           |
            | Drama             | Erótico           | Espionaje        | Experimental       |
            | Familiar          | Fantasía          | Fantástico       | Gótico             |
            | Histórico         | Infantil          | Maravilloso      | Melodrama          |
            | Misterio          | Mockumentary      | Musical          | Noir               |
            | Policíaco         | Road Movie        | Romance          | Slasher            |
            | Steampunk         | Superhéroes       | Suspenso         | Terror             |
            | Utopía            | Vampiros          | Western          | Zombies            |
            ---------------------------------------------------------------------------------
            """)
    
    while True:
        genero = input("Ingrese el genero la pelicula(Tiene que estar escrito tal cual como se muestra arriba): ")

        for generos_validar in lista_generos:
            
            if generos_validar == genero:
                
                return genero
        
        print("Ingreso de forma incorrecta el genero\n")      
#-------------------------------------------------------------------------------------------
def validar_anio() -> int:

    while True:
        anio = input("Ingrese el año de lanzamiento la pelicula: ")
        validar = anio.isdigit()

        if validar == True:
            anio = int(anio)

            if 1888 <= anio <= 2024:
                retorno = anio
                return retorno
            else:
                print("El año que ingreso no es valido (Tiene que estar entre 1888 y el año actual) y no tiene que se negativo")

        else:
            print("Error, el año que ingreso tiene letras debe tener solo numeros") 
#-------------------------------------------------------------------------------------------
def validar_titulo(lista_peliculas:list[str]) -> str:

    while True:
        titulo = input("Ingrese el nombre la pelicula: ")
        validar = True

        titulo_temporal = titulo.lower()
        longitud = len(titulo)
                
        if 0 < longitud <= 30:
            for titulo_existente in lista_peliculas:

                titulo_existente = titulo_existente["titulo"].lower()

                if titulo_existente == titulo_temporal:   
                    print("La pelicula ya esta agregada")
                    validar = False
        
            if validar == True:
                return titulo
            
        else:
            print("Error, verifique que el titulo no sea un espacio vacio o ingrese nada no sea mayor a 30 caracteres")
            titulo = input("Ingrese el nombre de su pelicula: ")
            longitud = len(titulo)     
#-------------------------------------------------------------------------------------------
def validar_plataforma() -> list[str]:

    lista = []

    while True:
        bandera = False
        plataforma = input("Ingrese en que plataforma en la que se encuentre su pelicula(si tiene mas de una ingrese una por una): ")
        longitud = len(plataforma)
        continuar = ""

        if  0 < longitud <= 20:
            for letra in plataforma:
                if letra.isnumeric() == True:
                    bandera = True

            if bandera == False:

                lista.append(plataforma)

                while continuar != "Si":
                    continuar = input("¿Desea seguir agregando? Si/No: ")
                    continuar = continuar.capitalize()
                        
                    if continuar == "No":
                        return lista
                    else: 
                        print("Debe ingresar Si/No")

            else:
                print("Error, la plataforma ingresada no debe contener numeros")

        else: 
            print("La plataforma ingresada no debe ser mayor a 20 caracteres")
#-------------------------------------------------------------------------------------------
def validar_duracion() -> int:

    while True:
        duracion = input("Ingrese la duracion de pelicula en minutos: ")
        numero = duracion.isnumeric()

        if numero == False:
            print("Debe ingresar solo numeros, no letras")
        
        else:
            duracion = int(duracion)
            if duracion > 0:
                    return duracion
            
            else:
                print("La duracion no puede ser 0")
#-------------------------------------------------------------------------------------------
def apliacion_principal() -> None:
    
    lista_peliculas = cargar_datos()
    
    while True:
        mostrar_menus("principal")
        opcion = input("Ingrese una opcion: ")
        
        match opcion:
            case "1":
                dar_de_alta(lista_peliculas)

            case "2": 
                print(modificar(lista_peliculas))
            
            case "3":
                print(eliminar(lista_peliculas))
            
            case "4":
                mostrar_peliculas(lista_peliculas)

            case "5":
                ordenar_peliculas(lista_peliculas)

            case "6":
                buscar_pelicula(lista_peliculas)
            
            case "7":
                sacar_promedio(lista_peliculas)

            case "8":
                menu_porcentajes(lista_peliculas)

            case "9":
                return           
#-------------------------------------------------------------------------------------------
def dar_de_alta(lista_peliculas:list[dict]) -> None:
    
    titulo = validar_titulo(lista_peliculas)
    genero = validar_genero()
    anio = validar_anio()
    duracion = validar_duracion()
    atp = validar_atp()
    plataforma = validar_plataforma()

    id_nueva = controlar_ids(lista_peliculas)

    diccionario = {
    "id": id_nueva,
    "titulo":titulo,
    "genero":genero,
    "año de lanzamiento":anio,
    "duracion":duracion,
    "atp":atp[1],
    "plataformas":plataforma}

    lista_peliculas.append(diccionario)

    retorno = f"Se agrego la pelicula {titulo} correctamente"
    return retorno
#-------------------------------------------------------------------------------------------
def modificar(lista_peliculas:list[dict]) -> str:
    
    while True:
    
        titulo = input("Ingrese el titulo que desea modificar: ")
        logitud = len(titulo)
        if logitud >= 30:
            for i in range(1, len(lista_peliculas)):

                if titulo == lista_peliculas[i]["titulo"]:

                    retorno = "No se hicieron cambios"
                    
                    while True:
                    
                        mostrar_menus("modificar")

                        opcion = input("Ingrese que quiere modificar: ")
                        opcion = opcion.upper()

                        match opcion:
                            case "A":
                                
                                titulo = validar_titulo(lista_peliculas)
                                retorno += modificar_caso(lista_peliculas[i], "titulo", retorno, titulo)
                            case "B":

                                genero = validar_genero()
                                retorno += modificar_caso(lista_peliculas[i], "genero", retorno, genero)
                            case "C":

                                anio = validar_anio()
                                retorno += modificar_caso(lista_peliculas[i], "año de lanzamiento", retorno, anio)  
                            case "D":

                                duracion = validar_duracion()
                                retorno += modificar_caso(lista_peliculas[i], "duracion", retorno, duracion)    
                            case "E":

                                atp = validar_atp()
                                retorno += modificar_caso(lista_peliculas[i], "atp", retorno, atp)   
                            case "F":

                                plataforma = validar_plataforma()
                                retorno += modificar_caso(lista_peliculas[i], "plataforma", retorno, plataforma)   
                            case "G":
                                return retorno
                            
                            case _: 
                                print("Error, Ingrese una opcion correcta")

        print("No se encontro una pelicula con ese nombre (Tiene que ser el nombre exacto)")    
#-------------------------------------------------------------------------------------------
def modificar_caso(diccionario_empleado:dict, clave:str, retorno: str, reemplazar:str) -> str:
    
    diccionario_empleado[clave] = reemplazar
    retorno = f"Se modifico el {clave} correctamente.\n"
    
    return retorno      
#-------------------------------------------------------------------------------------------
def eliminar(lista_pelicula:list[dict]) -> str:

    retorno = ""

    while True:
        pelicula = input("Ingrese la pelicula que quiere eliminar: ")

        for i in range(1, len(lista_pelicula)):
            if pelicula == lista_pelicula[i]["titulo"]:

                lista_pelicula.remove(lista_pelicula[i])
                retorno = "Pelicula eliminado correctamente"

                return retorno
        
        print("No se encontro una pelicula con ese nombre (Tiene que ser el nombre exacto): ")
#-------------------------------------------------------------------------------------------
def mostrar_peliculas(lista_peliculas:list[dict]) -> None:

    while True:
        mostrar_menus("mostrar peliculas")
        opcion = input("Ingrese una de las opciones: ")
        opcion = opcion.upper()

        match opcion:
            case "A":
                mostrar_informacion(lista_peliculas)

            case "B":  
                while True:
                    genero_buscar = validar_genero()
                    lista_genero = list(filter(lambda genero: genero["genero"] == genero_buscar, lista_peliculas))

                    if lista_genero != []:
                            mostrar_informacion(lista_genero)
                            break

                    else:
                        print("No hay peliculas con este genero, intente nuevamente \n")   

            case "C":
                while True:
                    año_buscar = validar_anio()
                    lista_año = list(filter(lambda año: año["año de lanzamiento"] == año_buscar, lista_peliculas))
                    
                    if lista_año != []:
                        mostrar_informacion(lista_año)
                        break

                    else:
                        print("No hay peliculas ingresadas con ese año, intente nuevamente \n") 
            
            case "D":

                lista_atp = list(filter(lambda atp: atp["atp"] == True, lista_peliculas))
                mostrar_informacion(lista_atp)

            case "E":
                
                lista_no_atp = list(filter(lambda atp: atp["atp"] == False, lista_peliculas))
                mostrar_informacion(lista_no_atp)

            case "F":
                while True:
                    
                    plataforma_buscar = validar_plataforma()
                    
                    lista_plataforma = list(filter(lambda plataforma: plataforma["plataforma"] == plataforma_buscar, lista_peliculas))
                    mostrar_informacion(lista_plataforma)

                    if lista_plataforma != []:
                        mostrar_informacion(lista_plataforma)
                        break

                    else:
                        print("No hay peliculas ingresadas con ese plataforma, intente nuevamente \n") 

            case "G":
                break
#-------------------------------------------------------------------------------------------
def mostrar_informacion(lista_peliculas:list[str]) -> None:
    print("*" * 148)
    print("|                       Título                     |       Género       |  Año de lanzamiento   |   Duración    |   ATP   |        Plataforma      |")
    print("-" * 148)

    for i in range(len(lista_peliculas)):

        titulo = lista_peliculas[i]["titulo"]
        genero = lista_peliculas[i]["genero"]
        año = lista_peliculas[i]["año de lanzamiento"]
        duracion = lista_peliculas[i]["duracion"]

        atp = lista_peliculas[i]["atp"]

        if atp == True:
            atp = "Si"
        else:
            atp = "No"

        plataforma = lista_peliculas[i]["plataforma"]
        separador = "-"
        plataforma = separador.join(plataforma)

        print(f"|{titulo:50}|{genero:20}|{año:23}|{duracion:11} min|{atp:9}|{plataforma:24}|")
    print("*" * 148)
#-------------------------------------------------------------------------------------------
def ordenar_peliculas(lista_peliculas:list[dict]) -> None:

    while True:

        mostrar_menus("ordenar peliculas")

        opcion = input("Ingrese como quiere ordenar a los empleados: ").upper()

        while opcion != "A" and opcion != "B" and opcion != "C" and opcion != "D" and opcion != "E":
                
                opcion = input("Ingrese como quiere ordenar a los empleados: ").upper()

        if opcion == "E":
                    return
        
        mostrar_menus("sub menu ordenar")
        
        opcion_2 = input("Ingrese de que forma lo quiere ordenar: ")

        while opcion_2 != "1" and opcion_2 != "2":
            opcion_2 = input("Ingrese de que forma lo quiere ordenar: ")

        match opcion:

            case "A":
                if opcion_2 == "1":
                    bubble_sort("ascendente", "titulo", lista_peliculas)
                else:
                    bubble_sort("descendente", "titulo", lista_peliculas)
            
            case "B": 
                if opcion_2 == "1":
                    bubble_sort("ascendente", "genero", lista_peliculas)
                else:
                    bubble_sort("descendente", "genero", lista_peliculas)
            
            case "C":
                if opcion_2 == "1":
                    bubble_sort("ascendente", "año de lanzamiento", lista_peliculas)
                else:
                    bubble_sort("descendente", "año de lanzamiento", lista_peliculas)

            case "D":
                if opcion_2 == "1":
                    bubble_sort("ascendente", "duracion", lista_peliculas)
                else:
                    bubble_sort("descendente", "duracion", lista_peliculas)             
#-------------------------------------------------------------------------------------------
def bubble_sort(orden:str , criterio:str, lista_empleados:list[dict]) -> None:

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
#-------------------------------------------------------------------------------------------    
def buscar_pelicula(lista_pelicula:list[dict]) -> str:

    while True:
        pelicula = input("Ingrese la pelicula que quiere eliminar: ")

        for i in range(1, len(lista_pelicula)):
            if pelicula == lista_pelicula[i]["titulo"]:

                lista_titulo = list(filter(lambda genero: genero["titulo"] == pelicula, lista_pelicula))

                if lista_titulo != []:
                    mostrar_informacion(lista_titulo)
                    break
            
        print(f"No se encontro la pelicula {pelicula}, intente nuevamente")
#-------------------------------------------------------------------------------------------
def sacar_promedio(lista_peliculas:list[dict]) -> None:
    
    while True:
        mostrar_menus("calcular promedio")

        opcion = input("Ingrese una opcion: ").upper()

        match opcion:
            case "A":
                print(promedios(lista_peliculas, "año de lanzamiento"))

            case "B":
                print(promedios(lista_peliculas, "duracion"))

            case "C":
                break
#-------------------------------------------------------------------------------------------
def promedios(lista_peliculas:list[dict], clave:str) -> str:

    total = 0

    for i in range(len(lista_peliculas)):
        
        total += lista_peliculas[i][clave]

    promedio = total / len(lista_peliculas) #puedo usar i pero no lo uso porque no se podria en otros lenguajes

    promedio = round(promedio)

    if clave == "duracion":

        clave = "minutos"
         
    retorno = f"El promedio total de {clave} es de: {promedio}"
    
    return retorno
#-------------------------------------------------------------------------------------------
def menu_porcentajes(lista_peliculas:list[dict]) -> None:
    
    while True:

        mostrar_menus("calcular porcentaje")
        opcion = input("Ingrese una opcion: ").upper()

        match opcion:
            case "A":

                mostrar_menus("porcentaje sub-menu")
                opcion_2 = input("Ingrese Que quiere mostrar: ")

                while opcion_2 != "1" and opcion_2 != "2" and opcion_2 != "3":
                    opcion_2 = input("Ingrese Que quiere mostrar: ")

                if opcion_2 == "1":
                    print(porcentaje_individual(lista_peliculas))
                
                elif opcion_2 == "2":
                    porcentajes_completo(lista_peliculas)
                
                else:
                    break

            case "B": 
                print(porcentaje_atps(lista_peliculas))

            case "C":    
                break
#-------------------------------------------------------------------------------------------
def porcentaje_individual(lista_peliculas:list[dict]) -> str:

    genero = validar_genero()

    total = len(lista_peliculas)

    cantidad_genero = list(filter(lambda pelicula : pelicula["genero"] == genero, lista_peliculas))

    parte = len(cantidad_genero)

    porcentaje = (parte/total) * 100

    porcentaje = round(porcentaje)

    mensaje = f"Genero: {genero} | Porcentaje: {porcentaje}%"
    
    return mensaje
#-------------------------------------------------------------------------------------------
def porcentajes_completo(lista_peliculas:list[dict]):
    lista_generos = ["Acción","Aventura", "Animación", "Biográfico", "Comedia", "Comedia romántica", "Comedia dramática",
                    "Crimen", "Documental", "Drama", "Fantasía", "Histórico", "Infantil", "Musical", "Misterio", "Policíaco", "Romance",
                    "Ciencia ficción", "Suspenso", "Terror", "Western", "Bélico", "Deportivo", "Noir", "Experimental", "Familiar",
                    "Superhéroes", "Espionaje", "Artes marciales", "Fantástico", "Catástrofe", "Melodrama", "Erótico", "Cine"
                    "independiente", "Zombies", "Vampiros", "Cyberpunk", "Steampunk", "Distopía", "Utopía", "Road Movie",
                    "Docuficción", "Mockumentary", "Gótico", "Slasher", "Adolescente", "Culto", "Maravilloso"]
    
    total = len(lista_peliculas)

    for genero in lista_generos:

        cantidad_genero = list(filter(lambda pelicula : pelicula["genero"] == genero, lista_peliculas))

        if cantidad_genero != []:
            parte = len(cantidad_genero)

            porcentaje = (parte/total) * 100

            porcentaje = round(porcentaje)

            mensaje = f"Genero: {genero} | Porcentaje: {porcentaje}%"

        else:

            mensaje = f"Genero: {genero} | No hay peliculas sobre este genero"

        print(mensaje)
#-------------------------------------------------------------------------------------------
def porcentaje_atps(lista_peliculas:list[dict]):

    total = len(lista_peliculas)

    lista_atp = list(filter(lambda pelicula : pelicula["atp"] == True, lista_peliculas))

    parte = len(lista_atp)

    porcentaje = (parte/total) * 100

    porcentaje = round(porcentaje)

    resto = 100 - porcentaje

    print(f"Peliculas con atp | Porcentaje: {porcentaje}%")
    print(f"Peliculas sin atp | Porcentaje: {resto}%")
#-------------------------------------------------------------------------------------------
apliacion_principal()