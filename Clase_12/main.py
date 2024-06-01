
from class_video import *

"""
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""

#--------------------------------------------------------------------------------------         

validar= False

while True:
    print("""
             A. NORMALIZAR OBJETOS
             B. MOSTRAR TEMAS
             C. ORDENAR TEMAS
             D. PROMEDIO DE VISTAS
             E. MAXIMA REPRODUCCION
             F. BUSQUEDA POR CODIGO
             G. LISTAR POR COLABORADOR
             H. EXIT""")
    opcion=input("ingrese su opcion: ").upper()
    match opcion:
        case "A":
            validar = True
            pass
        case "B":
            if validar ==True:
                print()
            else:
                print("Debe ingresar primero la Opcion A")
            pass
        case "C":
            if validar ==True:
                pass
            else:
                print("Debe ingresar primero la Opcion A")
            pass
        case "D":
            if validar ==True:
                pass
            else:
                print("Debe ingresar primero la Opcion A")
            pass
        case "E":
            if validar ==True:
                pass
            else:
                print("Debe ingresar primero la Opcion A")
            pass
        case "F":
            if validar ==True:
                pass
            else:
                print("Debe ingresar primero la Opcion A")
            pass
        case "G":
            if validar ==True:
                pass
            else:
                print("Debe ingresar primero la Opcion A")
            pass
        case "H":
            break
        
        
        case _:
            print("ingrese una opcion correcta")
