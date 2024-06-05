def print_lindo(lista:str) -> None:
    for linea in lista:
        
        print(linea)

def print_nombre_lindo(lista: list[dict])->None:
    print("- LISTA MAYORES -")
    for persona in lista:
        print(f"Nombre: {persona['nombre']} | Edad: {persona['edad']}")


lista_numeros = [1,2,3,4,5,6,7,8,9,10]

#2.A_________________________________________________________________
print("_________________________________________________________________")

print("2.A")
lista_cuadrados = map(lambda numero : numero ** 2, lista_numeros)

lista_cuadrados = list(lista_cuadrados)

print_lindo(lista_cuadrados)

print("_________________________________________________________________")

#2.B_________________________________________________________________

print("2.B")
lista_pares = filter(lambda numero: numero % 2 == 0, lista_numeros)

lista_pares= list(lista_pares)

print_lindo(lista_pares)

print("_________________________________________________________________")
#2.C_________________________________________________________________

print("2.C")
palabras = ['hola', 'mundo', 'python', 'lambda']

lista_mayusculas = map(lambda str:str.upper(), palabras)

lista_mayusculas = list(lista_mayusculas)

print_lindo(lista_mayusculas)

print("_________________________________________________________________")
#2.D_________________________________________________________________

print("2.D")
palabras = ['¡hola!', 'mundo?', 'python', 'lambda', 'pedro73']

palabras_alpha = filter(lambda palabra: palabra.isalpha(), palabras)

palabras_alpha = list(palabras_alpha)

print_lindo(palabras_alpha)

print("_________________________________________________________________")

#E.1_________________________________________________________________

print("3.1")
personas = [
    {'nombre': 'Juan', 'edad': 15},
    {'nombre': 'Ana', 'edad': 22},
    {'nombre': 'Pedro', 'edad': 19},
    {'nombre': 'María', 'edad': 17},
    {'nombre': 'Laura', 'edad': 20}
]


mayores = filter(lambda personas : personas["edad"] >= 18, personas)

mayores = list(mayores)

print_nombre_lindo(mayores)

print("_________________________________________________________________")
#.3.2_________________________________________________________________

print("3.2")
nombre_mayuscula = map(lambda persona : persona["nombre"].upper(), personas)

nombre_mayuscula = list(nombre_mayuscula)

print_lindo(nombre_mayuscula)

print("_________________________________________________________________")

