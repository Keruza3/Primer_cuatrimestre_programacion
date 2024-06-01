from data_stark import *
from funciones_reutilizadas import *
from funciones_menu import *

def stark_marvel_app(lista_heroes:list) -> None:

    bandera = False
    
    while True:

        numero = stark_menu_principal()

        match numero:
            case 1:

                if stark_normalizar_datos(lista_heroes) == True:

                    bandera = True

                    print("Datos normalizados")

                else:

                    print("Los datos ya estan normalizados")
        
            case 2:
                if bandera == True:
                    
                    opcion_2(lista_heroes)
                    
                else:
                    
                    print("Tiene que normalizar los datos en la opcion 1")
            
            case 3:
                if bandera == True:
                    
                    opcion_3_4_5_6(lista_personajes,"F", "altura")
            
                else:
                    
                    print("Tiene que normalizar los datos ")
            
            case 4:
                if bandera == True:
                    
                    opcion_3_4_5_6(lista_personajes, "M", "altura")
            
                else:
                    
                    print("Tiene que normalizar los datos ")
            
            case 5:
                if bandera == True:
                    opcion_3_4_5_6(lista_personajes, "M", "fuerza")
            
                else:
                    
                    print("Tiene que normalizar los datos ")
            
            case 6:
                if bandera == True:
                    opcion_3_4_5_6(lista_personajes, "NB", "fuerza")
            
                else:
                    
                    print("Tiene que normalizar los datos ")

            case 7:
                if bandera == True:
                    opcion_7(lista_personajes)
            
                else:
                    
                    print("Tiene que normalizar los datos ")

            case 8:
                if bandera == True:
                    opcion_8_9(lista_personajes, "color_ojos")
            
                else:
                    
                    print("Tiene que normalizar los datos ")
            
            case 9:
                if bandera == True:
                    
                    opcion_8_9(lista_personajes, "color_pelo")
            
                else:
                    
                    print("Tiene que normalizar los datos ")
            
            case 10:
                if bandera == True:
                    opcion_10_11(lista_personajes, "color_ojos")
            
                else:
                    
                    print("Tiene que normalizar los datos ")

            case 11:
                if bandera == True:
                    
                    opcion_10_11(lista_personajes, "inteligencia")  
            
                else:
                    
                    print("Tiene que normalizar los datos ")

stark_marvel_app(lista_personajes)