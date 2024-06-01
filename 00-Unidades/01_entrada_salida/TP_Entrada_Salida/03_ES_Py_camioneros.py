import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''
nombre: Juan Ignacio 
apellido: Ullua
---
TP: ES_Camioneros
---
Enunciado:

3.	Para el departamento de logística:

	A.	Es necesario saber la cantidad camiones que harian falta para transportar los materiales que se utilizarán para la construcción de un edificio. Para ello, se ingresa la cantidad de toneladas necesarias de materiales a transportar. El programa deberá informar la cantidad de camiones, sabiendo que cada uno de ellos puede transportar por viaje 3500kg

    B.	A partir del ingreso de la cantidad de kilómetros que tiene que recorrer estos camiones para llegar al destino de la obra, necesitamos que el programa informe cual es el tiempo (en horas) que tardará cada uno de los camiones, si sabemos que cada camión puede ir a una velocidad máxima y constante de 90 km/h  

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Toneladas")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_toneladas = customtkinter.CTkEntry(master=self)
        self.txt_toneladas.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Kilómetros")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_kilometros = customtkinter.CTkEntry(master=self)
        self.txt_kilometros.grid(row=1, column=1)
       
        self.btn_cantidad_camiones = customtkinter.CTkButton(master=self, text="Calcular cantidad de camiones", command=self.btn_cantidad_camiones_on_click)
        self.btn_cantidad_camiones.grid(row=3, pady=10, padx=30 ,columnspan=2, sticky="nsew")
        
        self.btn_tiempo_llegada = customtkinter.CTkButton(master=self, text="Calcular tiempo de llegada", command=self.btn_tiempo_llegada_on_click)
        self.btn_tiempo_llegada.grid(row=4, pady=10, padx=30, columnspan=2, sticky="nsew")
    
    """
    1 camion = 3500kg
    
    el camion va a 90 km/h
    """
    
    
    def btn_cantidad_camiones_on_click(self):
      
      toneladas = (self.txt_toneladas.get())

      toneladas = float(toneladas)
      
      kilos = (toneladas * 1000)

      camiones = (kilos / 3500)

      camiones = math.ceil(camiones)

      mensaje = f"Para la cantidad de: {toneladas} toneladas, va a necesitar  {camiones} camiones"
      
      alert ("TP Camioneros" , mensaje)

      


    def btn_tiempo_llegada_on_click(self):
      
      kilometros = (self.txt_kilometros.get())

      kilometros = float(kilometros)

      horas_parte_entera = (kilometros // 90)

      minutos = (kilometros % 90 ) 

      mensaje = f"El recorrido de: {kilometros}  km va a tardar {horas_parte_entera} horas y  {minutos}   Minutos" #:.0f para poner solo tantos decimales como yo quiera
    
      alert("TP Camioneros" , mensaje)

# // te devuelve la parte entera de una divsion
# % te devuelve el resto

    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()