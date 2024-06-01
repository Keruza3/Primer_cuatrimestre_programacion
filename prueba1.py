import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Ignacio
apellido: Ullua
---
Enunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
edad(mayor a 0)
pedir datos por prompt y mostrar por print
Punto A-informar cual fue el sexo mas ingresado
Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

DNI terminados en  8 o 9

1))informar la cantidad de personas menores de edad (menos de 18 años)
2)la temperatura promedio en total de todas las personas menores de edad
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)

Todos los alumnos: 
B-informar cual fue el sexo mas ingresado
C-el porcentaje de personas con fiebre y el porcentaje sin fiebre


'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        contador_m = 0
        contador_f = 0
        contador_nb = 0
        fiebre = 0
        no_fiebre = 0
        menor = 0
        bandera_primer_F= True
        
        for personas in range(0 , 5):
        
            nombre = prompt("" , "Ingrese su nombre")

            temperatura = prompt("" , "Ingrese su temperatura (entre 35 y 42)")
            temperatura = int(temperatura)
            while 35 > temperatura or temperatura > 42: 
                    temperatura = prompt("" , "Ingrese su temperatura (entre 35 y 42)")
                    temperatura = int(temperatura)
            if temperatura < 38:
                
                no_fiebre += 1
            else:
                fiebre += 1
        



            sexo = prompt("" , "Ingrese su sexo F - M - NB")
            sexo = sexo.upper()
            while sexo != "F" and sexo  != "M" and sexo != "NB":
                sexo = prompt("" , "Ingrese su sexo F - M - NB")
                sexo = sexo.upper()
                match sexo:
                    case "F":
                        contador_f += 1
                        temperatura_f = temperatura
                        bandera_primer_F = False
                    case "M":
                        contador_m += 1
                    case "NB":
                        contador_nb += 1


            edad = prompt("" , "Ingrese su edad")
            edad = int(edad)
            while edad < 0:
                edad = prompt("" , "Ingrese su edad")
                edad = int(edad)
                if edad < 18:
                    menor += 1
                    acumulador_temp = temperatura + acumulador_temp


            #el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)
        
            
            if bandera_primer_F == False:
                nombre_F = nombre
                temperatura_m = int(temperatura_f)
                bandera_primer_F = True

                if int(temperatura_f) < int(temperatura_m):
                    nombre_F = nombre
                    temperatura_m = int(temperatura_f)
            
            
            seguir = question("" , "Desea continuar?")
            if seguir == False:
                break


        if bandera_primer_F == True:
            mensaje_tres = f"el nombre de la persona de sexo  femenino es {nombre_F} con la temperatura mas baja de {temperatura_f}"
            print(mensaje_tres)


                


        #Punto A-informar cual fue el sexo mas ingresado
        if  contador_f > contador_m  > contador_nb:
                mensaje = f"el sexo mas ingresado fue Femenino con {contador_f} personas"
        else:
            if contador_m > contador_nb:
                mensaje = f"el sexo mas ingresado fue Masculino con {contador_m} personas"
            else:
                mensaje = f"el sexo mas ingresado fue no Binario con {contador_nb}"

        print(mensaje)

        #Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

        Porcentaje_No_F  = (no_fiebre * 100) / personas
        mensaje_B = f"el porcentaje de personas sin fiebre es de {Porcentaje_No_F}"
        print(mensaje_B)

        Porcentaje_F  = (fiebre * 100) / personas
        mensaje_B = f"el porcentaje de personas con fiebre es de {Porcentaje_F}"
        print(mensaje_B)

        #informar la cantidad de personas menores de edad (menos de 18 años)

        mensaje_uno = f"la cantidad de personas menores de edad son de {menor}"
        print(mensaje)

        #la temperatura promedio en total de todas las personas menores de edad
            
        promedio_menor_temp = acumulador_temp / menor
        mensaje_dos = f"La temperatura promedio en total de los menores es de {promedio_menor_temp}"
        print(mensaje_dos)

       


"""    
nombre
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
edad(mayor a 0)
pedir datos por prompt y mostrar por print
Punto A-informar cual fue el sexo mas ingresado
Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

DNI terminados en  8 o 9

1))informar la cantidad de personas menores de edad (menos de 18 años)
2)la temperatura promedio en total de todas las personas menores de edad
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)

Todos los alumnos: 
B-informar cual fue el sexo mas ingresado
C-el porcentaje de personas con fiebre y el porcentaje sin fiebre
"""
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()