import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Ignacio
apellido: Ullua
---
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        
      
       sexo = input("Ingrese el sexo de su mascota: ")import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Ignacio
apellido: Ullua
---
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        
        seguir = True
        contador_M = 0
        contador_F = 0
        contador_mascotas = 0
        contador_gato = 0
        contador_perro = 0
        contador_exotico = 0
        bandera_primer_mascota = False
        bandera_perro = False
        acumulador_peso = 0
        bandera_perro_mensaje = False

        while seguir == True:

            contador_mascotas += 1



            nombre = prompt("" , "Nombre de la mascota")
        
            tipo = prompt("" , "Tipo de animal (Gato , Perro o exotico)")
            tipo = tipo.upper()
            if tipo != "GATO" and tipo != "PERRO" and tipo != "EXOTICO":
                tipo = prompt("" , "Tipo de animal (Gato , Perro o exotico)")
                tipo = tipo.upper()
            
            match tipo:
                case "GATO":
                    contador_gato += 1
                case "PERRO":
                    contador_perro += 1
                    bandera_perro = True
                    bandera_perro_mensaje = True
                case "EXOTICO":
                    contador_exotico += 1

            
            peso = prompt("" , "Ingrese el peso")
            peso = int(peso)
            if peso < 10 or peso > 80:
                peso = prompt("" , "Ingrese el peso")
                peso = int(peso)
            else:
                acumulador_peso = acumulador_peso + peso


            sexo = prompt("" , "El sexo del animal es:")
            sexo = sexo.upper()
            if sexo != "F" and sexo != "M":
                sexo = prompt("" , "El sexo del animal es (F o M)")
                sexo = sexo.upper()
            match sexo:
                case  "F":
                    contador_F += 1
                
                case "M":
                    contador_M += 1


            edad = prompt("" , "Edad de la mascota")
            edad = int(edad)
            if edad <= 0: 
                edad = prompt("" , "Edad de la mascota")
                edad = int(edad)


            seguir = question("" , "Desea continuar")
            if seguir == None:
                seguir = False



            #Informe D- El nombre del perro más joven
            if bandera_perro == True:
                nombre_final_perro = nombre
                edad_perro = edad
                bandera_perro = False
            else:
                if tipo == "PERRO":
                    if edad < edad_perro:
                        edad_perro = edad
                        nombre_final_perro = nombre

            if bandera_perro_mensaje == True:
                mensaje_d = f"El nombre del perro más joven es {nombre_final_perro} y tiene una edad de {edad_perro}"
                print(mensaje_d)

            

            #Informe C- El nombre y tipo de la mascota menos pesada

            if bandera_primer_mascota == False:
                nombre_final = nombre
                peso_menor = peso
                tipo_final = tipo
                bandera_primer_mascota = True

            else:
                 if  peso < peso_menor:
                        nombre_final = nombre
                        peso_menor = peso
                        tipo_final = tipo

        mensaje_c = f"la mascota menos pesada pesa: {peso_menor} kgs, su nombre es {nombre_final} y su tipo es: {tipo_final}"
        


            

            
        #Informe A- Cuál fue el sexo menos ingresado (F o M)

        if contador_F < contador_M:
            mensaje_a = f"el sexo menos ingresado fue F con {contador_F} mascotas"

        else:
            contador_M < contador_F
            mensaje_a = f"el sexo menos ingresado fue M con {contador_M} mascotas"

        


       #Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
        

        Porcentaje_perro  = (contador_perro * 100) / contador_mascotas

        Porcentaje_gato = (contador_gato * 100) / contador_mascotas

        Porcentaje_exotico = (contador_exotico * 100) / contador_mascotas

        mensaje_b = f"""El porcentaje de mascotas que hay por tipo:
        gato {Porcentaje_gato}%
        perro {Porcentaje_perro}%
        exotico {Porcentaje_exotico}%"""

        

        #Informe E- El promedio de peso de todas las mascotas

        
        promedio_peso = acumulador_peso / contador_mascotas

       
        
        
        
        
        mensaje_e = f"El promedio de peso de todas las mascotas es de {promedio_peso}kgs"

        print(mensaje_a)
        print(mensaje_b)
        print(mensaje_c)
        #print(mensaje_d) lo comento porque se tiene que cumplir una condicion para que de el mensaje
        print(mensaje_e)
    

    
    
'''
mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas
'''
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()