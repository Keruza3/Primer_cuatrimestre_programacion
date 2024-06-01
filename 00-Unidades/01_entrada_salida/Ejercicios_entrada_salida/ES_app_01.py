import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Ignacio
apellido: Ullua
---
Ejercicio dojo 01
(E/S)
para saber el costo de un viaje necesitamos el siguiente algoritmo,
sabiendo que el precio por kilo de pasajero es 1000 pesos
Se ingresan todos los datos por PROMPT
los datos a solicitar de dos personas son,
nombre, edad y peso
se pide  armar el siguiente mensaje
"hola german y marina , sus pesos son 80 kilos y 60 kilos respectivamente
, sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos  

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
     
        precio_kilo = 1000
        
        nombre_uno = prompt("titulo", "ingrese su nombre")
        
        edad_uno = prompt("titulo" , "ingrese su edad")
        
        edad_uno = int(edad_uno)
        
        peso_uno = prompt("titulo" , "ingrese su peso")
        
        peso_uno = int(peso_uno)

        nombre_dos = prompt("titulo" , "ingrese su nombre")
        
        edad_dos = prompt("titulo" , "ingrese su edad")
        
        edad_dos = int(edad_dos)
        
        peso_dos = prompt ("titulo" , "ingrese peso")
        
        peso_dos = int(peso_dos)

        suma_peso = peso_uno + peso_dos 
        
        precio_viaje = suma_peso * 1000
        
        promedio = edad_uno + edad_dos / 2

        mensaje = f"Hola {nombre_uno} y {nombre_dos} , sus pesos son {peso_uno} kilos y {peso_dos} kilos respectivamente sumados da {suma_peso} kilos , el promedio de edad es  {promedio} y su viaje vale {precio_viaje} pesos"

        alert("ejercicio 1 sabado 2" , mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
