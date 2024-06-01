from data_stark import lista_personajes
import json

for heroe in lista_personajes:
    print(f"{heroe['nombre']}")

#write

archivo = open("Clases_Ejercicios/clase_15_archivos/archivo.txt", "w")
for heroe in lista_personajes:
    texto = f"{heroe['nombre']}\n"
    archivo.write(texto)

archivo.close()

#writelines


lista_heroes = []
for heroe in lista_personajes:
    lista_heroes.append(f"{heroe['nombre']}\n")

archivo = open("archivo_2.txt", "w")
archivo.writelines(lista_heroes)
archivo.close()


# #read (por bytes / 1 byte = 1 caracter)

archivo = open("archivo_2.txt", "r")
texto_1 = archivo.read(15)
archivo.close()

print(texto_1)


# #readline (bytes y cursos)
archivo = open("archivo_2.txt", "r")
texto_1 = archivo.readline()
archivo.close()
print(texto_1)


# #readlines (devuelve una lista de strings)
archivo = open("archivo_2.txt", "r")
contenido = archivo.readlines()
archivo.close()

for i in range(len(contenido)):
    print(contenido[i], end = "")


#seek / tell(devuelve int de donde esta el puntero)
archivo = open("archivo_2.txt", "r")
print(archivo.tell())
print(archivo.readline(), end = "")
archivo.close()



#with / seek / tell

with open("archivo.txt", "r") as archivo:
    print(archivo.tell())
    archivo.seek(3) #donde se para el puntero
    print(archivo.read())

#cada administrador de contexto abre de manera propia arrancando en 0

#DE PY A CSV
def guardar_csv_personas(lista_personas:list[dict], path:str):
    with open(path, 'w') as archivo:

        archivo.write('Nombre', 'Apellido', 'Edad', 'Dni \n')
        for i in range(len(lista_personas)):
            persona = lista_personas[i]
            nombre = persona['nombre']
            apellido = persona['apellido']
            edad =  persona['edad']
            dni = persona['dni']
            
            archivo.write(f"{nombre},{apellido},{edad},{dni}\n")


#DE CSV A PY
def cargar_personas_csv(path:str)-> list[dict]:
    with open(path, 'r') as archivo:
        lineas = archivo.readlines()
      

    lista_personas = []
    for i in range(1, len(lineas)):
        datos = lineas[i]
        datos.split(',')
        
        nombre = datos[0]
        apellido = datos[1]
        edad = int(datos[2])
        dni = datos[3]
        dni = dni.replace("\n","")
        dni = int(dni)

        persona = {"nombre": nombre,
                   "apellido": apellido,
                   "edad": edad,
                   "dni": dni}

        lista_personas.append(persona)
    
    return lista_personas


#.JSON()
