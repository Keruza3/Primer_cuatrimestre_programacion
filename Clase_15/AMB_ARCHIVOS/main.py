from funciones_validar import *
from funciones_menu import *

#Tuve un error grande al hacer el codigo porque yo al momento de manejarme con el archivo tipo json cuando empece el programa no lo tenia muy claro entonces segui trabajando todo con el csv 
#y cuando termine el codigo lo quise implementar y no podia ya que tenia que cambiar gran parte del codigo para hacerlo y como ya es de noche no tengo el tiempo.
#si les sirve de algo de tanto que intente arreglarlo me quedo muy claro el json ahora y el codigo funciona bastante bien(se crean archivos si no estan, se valida casi todo y si borro al
#ultimo usuario el siguiente se crea con el id que le sigue) que eran las cosas mas importantes. No me va a pasar mas ya aprendi
#-----------------------------------------------------------------------------------------------------
def aplicacion_principal() -> None:

    bandera = False

    while True:

        mostrar_menu("principal")

        opcion = input("Ingrese una opcion: ")
        
        match opcion:
            
            case "1":
                lista_empleados = json_csv()

                bandera = True
                
            case "2":
                if bandera == True:

                    ultima_id = controlar_ids()
                    crear_empleado(ultima_id, lista_empleados)

                else:
                    print("Primero debe leer desde un tipo de archivo")
            
            case "3":
                if bandera == True:

                    print(modificar(lista_empleados))
                    
                else:
                    print("Primero debe leer desde un tipo de archivo")

            case "4":
                if bandera == True:
                    
                    print(eliminar())
                else:
                    
                    print("Primero debe leer desde un tipo de archivo")

            case "5":
                if bandera == True:
                    imprimir_empleados("opcion 5")
    
                else:
                    print("Primero debe leer desde un tipo de archivo")

            case "6":
                if bandera == True:

                    imprimir_empleados("opcion 6")

                else:
                    print("Primero debe leer desde un tipo de archivo")
            
            case "7":
                if bandera == True:

                    imprimir_empleados("opcion 7")          
                else:
                    print("Primero debe leer desde un tipo de archivo")

            case "8":
                if bandera == True:
                    print(calcular_salario_promedio())
              
                else:
                    print("Primero debe leer desde un tipo de archivo")

            case "9":
                if bandera == True:
                    
                    ordenar_empleados()

                else:
                    print("Primero debe leer desde un tipo de archivo")

            case "10":
                
                print(
                """
                \n
                -----------------------------------
                !Gracias por utilizar el programa!
                -----------------------------------
                \n
                """)
                break
aplicacion_principal()