from funciones_validar import *
from funciones_recursivas import *
from funciones_menu import *


def aplicacion_principal() -> None:

    ids = 0

    bandera = False

    while True:

        mostrar_menu("principal")

        opcion = int(input("Ingrese una opcion: "))
        
        match opcion:
            
            case 1:

                ids += 1
                agregar_empleado(crear_empleado(ids), lista_empleados)

                bandera = True
                

            case 2:

                if bandera == True:
                    print(modificar(lista_empleados))

                else:
                    print("debe primero dar de alta una persona")
            
            case 3:

                if bandera == True:
                    
                    eliminar(lista_empleados)
                    
                    
                else:
                    print("debe primero dar de alta una persona")
            case 4:

                if bandera == True:
                    mostrar_empleados(lista_empleados)

                else:
                    print("debe primero dar de alta una persona")
            case 5:

                if bandera == True:
                    mostrar_gerente(lista_empleados)

                else:
                    print("debe primero dar de alta una persona")
            case 6:
                if bandera == True:
                    print(calcular_promedio(lista_empleados, "Salario") )
                    
                else:
                    print("debe primero dar de alta una persona")
                    
            case 7:
                print("""\n
    -----------------------------------
    !Gracias por utilizar el programa!
    -----------------------------------
    \n""")

            case _: 
                print("##ERROR##")
                         
            
aplicacion_principal()