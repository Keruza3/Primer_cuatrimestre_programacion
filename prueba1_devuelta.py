contador_F = 0
contador_M = 0

contador_perro = 0
contador_gato = 0
contador_exotico = 0


bandera_menos_peso = True
perro_bandera = True


perro_mas_joven = ""
edad_perro_joven = 0

peso_total = 0  


for _ in range(5):
        
            nombre = input("Ingrese el nombre de su mascota: ")

            tipo = input("Que tipo de mascota tiene: ")
            
            tipo = tipo.upper()
            
            while tipo != "GATO" and tipo != "PERRO" and tipo != "EXOTICO":
                
                tipo = input("Que tipo de mascota tiene: ")
            
                tipo = tipo.upper()

            peso = input("Ingrese el peso: ")
            
            peso = int(peso)

            while 10 > peso or peso > 80:
                 
                peso = input("Ingrese el peso: ")
                 
                peso = int(peso)

            sexo = input("Ingrese el sexo de su mascota: ")

            sexo = sexo.upper()
            
            while sexo != "F" and sexo != "M":

                sexo = input("Ingrese el sexo de su mascota: ")

                sexo = sexo.upper()

            edad = input("Ingrese la edad de su mascota: ")

            edad = int(edad)

            while edad < 0:
            
                edad = input("Ingrese la edad de su mascota: ")

                edad = int(edad)
            

            #Parte punto B y D
            
            match tipo:
                 case "EXOTICO":
                      contador_exotico += 1

                 case "GATO":
                      contador_gato += 1
                 
                 case "PERRO":
                      contador_perro += 1
                      if perro_bandera == True:
                            perro_mas_joven = nombre
                            edad_perro_joven = edad
                            edad_perro_joven = False

                      else:
                           if edad < perro_mas_joven:
                                perro_mas_joven = nombre
                                edad_perro_joven = edad
            
            #punto E

            peso_total += peso

            
                   
                     
            
            
            
            
            #punto A
            match sexo:
                case "F":
                    contador_F += 1

                case "M":
                    contador_M += 1
            
             #punto C

            if bandera_menos_peso == True:

                peso_menor = peso

                nombre_menos = nombre

                tipo_menos = tipo

                bandera_menos_peso = False

            else:
                 
                 if peso < peso_menor:
                    peso_menor = peso

                    nombre_menos = nombre

                    tipo_menos = tipo
            
            
                
                
                 

                
                 

                    

        
if contador_F > contador_M:
            
    contador_mayor_sexo = contador_F
        
else:
            
    contador_mayor_sexo = contador_M

    #punto B

porcentaje_exotico = (contador_exotico / 5 ) * 100

porcentaje_perro = (contador_perro / 5 ) * 100

porcentaje_gato = (contador_gato / 5) * 100

    #punto D
    #mensaje a hacer








    
    
'''
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas
'''