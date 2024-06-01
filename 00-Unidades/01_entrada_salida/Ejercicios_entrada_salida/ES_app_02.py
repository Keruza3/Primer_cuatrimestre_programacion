import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Ignacio
apellido: Ullua
---
Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

Nombre

Edad (debe ser mayor a 12)

Altura (no debe ser negativa)

Días que asiste a la semana (1, 3, 5)

Kilos que levanta en peso muerto (no debe ser cero, ni negativo)

No sabemos cuántos clientes serán consultados.

Se debe informar al usuario:

El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.

El porcentaje de clientes que asiste solo 1 día a la semana.

Nombre y edad del cliente con más altura.

Determinar si los clientes eligen más ir 1, 3 o 5 días

Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista

5 días a la semana.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        condicion_seguir = True
        contador_dia_uno = 0
        contador_dia_tres = 0
        acumulador_peso = 0   
        contador_personas_totales = 0
        contador_dia_cinco = 0
        bandera_primer_numero = False
        while condicion_seguir == True:
          
            contador_personas_totales += 1          
            nombre = prompt("" , "Ingrese su nombre")

            edad = prompt("" , "Ingrese su edad")
            edad = int(edad)
            if edad < 12:
                edad = prompt("" , "Ingrese su edad")
                edad = int(edad)

            altura = prompt("" , "Ingrese su  altura")
            altura = int(altura)
            if altura < 0:
                altura = prompt("" , "Ingrese su  altura")
                altura = int(altura)
            
            dias = prompt("" , "Ingrese los dias que desea ir")
            if dias != "1" and dias != "3" and dias != "5":
                dias = prompt("" , "Ingrese los dias que desea ir")
            else:
                match dias:
                    case "3":
                        contador_dia_tres += 1
                    case "1":
                        contador_dia_uno +=1
                    case "5":
                        contador_dia_cinco +=1
            
            kilos_levantados = prompt("" , "Ingrese cuanto levanta en peso muerto")
            kilos_levantados = int(kilos_levantados)
            if kilos_levantados <= 0:
                kilos_levantados = prompt("" , "Ingrese cuanto levanta en peso muerto")
                kilos_levantados = int(kilos_levantados)
            
            condicion_seguir = question("" , "Desea continuar?")
            if condicion_seguir == None:
                condicion_seguir = False




            #El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
                
            
            if dias == 3:
                acumulador_peso = acumulador_peso + kilos_levantados
                promedio_kilos = acumulador_peso / contador_dia_tres

                mensaje = f"El promedio de kilos que levantan las personas que asisten solo 3 días a la semana es de: {promedio_kilos}"
            else:
            #El porcentaje de clientes que asiste solo 1 día a la semana.
                
                if dias == 1:
                    porcentaje = contador_dia_uno * 100/ contador_personas_totales
                    mensaje = f"El porcentaje de clientes que asiste solo 1 día a la semana. es de  el {porcentaje}%"


            #Nombre y edad del cliente con más altura.
            if bandera_primer_numero == False:
                    maximo = altura
                    nombre = nombre
                    edad = edad
                    bandera_primer_numero = True
                    mensaje = f"cliente con más altura es de {maximo}mts, su nombre es {nombre} y la edad es {edad}"
            else:
                if altura > maximo:
                    maximo = altura
                    nombre = nombre
                    edad = edad
                    mensaje = f"cliente con más altura es de {maximo}mts, su nombre es {nombre} y la edad es {edad}"

            #Determinar si los clientes eligen más ir 1, 3 o 5 días
                    
        if contador_dia_cinco > contador_dia_tres > contador_dia_uno:
            mensaje = f"los clientes eligen más ir el dia 5 con {contador_dia_cinco} personas"
        else:
            if contador_dia_tres > contador_dia_uno:
                mensaje = f"los clientes eligen más ir el dia 3 con {contador_dia_tres} personas"
            else:
                mensaje = f"los clientes eligen más ir el dia 1 con {contador_dia_uno} personas"
            
            #Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que 
            #solo asista 5 días a la semana.
            
            if edad == 5:
                if bandera_primer_numero == False:
                    maximo = edad
                    nombre = nombre
                    kilos_levantados = kilos_levantados
                    bandera_primer_numero = True
                    mensaje = f"cliente con menor edad es de {maximo}mts, su nombre es {nombre} y los kilos levantados son {kilos_levantados}"
                else:
                    if edad < maximo:
                        maximo = edad
                        nombre = nombre
                        kilos_levantados = kilos_levantados
                        mensaje = f"cliente con menor edad es de {maximo}mts, su nombre es {nombre} y los kilos levantados son {kilos_levantados}"
        
"""
nombre

Edad (debe ser mayor a 12)

Altura (no debe ser negativa)

Días que asiste a la semana (1, 3, 5)

Kilos que levanta en peso muerto (no debe ser cero, ni negativo)

No sabemos cuántos clientes serán consultados.

Se debe informar al usuario:

El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.

El porcentaje de clientes que asiste solo 1 día a la semana.

Nombre y edad del cliente con más altura.

Determinar si los clientes eligen más ir 1, 3 o 5 días

Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista

5 días a la semana. """

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
         
