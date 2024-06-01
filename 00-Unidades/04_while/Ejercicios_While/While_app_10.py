import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Ignacio
apellido: Ullua
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        contador_ceros = 0
        numero_total_resta = 0
        numero_total_suma = 0
        cantidad_numero_suma= 0
        cantidad_numero_resta = 0 
        diferencia_suma_y_resta = 0

        while True:
            
            numero = prompt("ej 10 while" , "Ingreso de números (presione Cancelar para finalizar):")
            
            

            if numero == None:
                
                break

            else:
                numero = int(numero)
                if numero >0:
                    
                        
                        numero_total_suma = numero + numero_total_suma

                        cantidad_numero_suma += 1
                else:
                    if numero <0:
                        
                        numero_total_resta = numero + numero_total_resta
                        cantidad_numero_resta += 1 
                    else:
                       
                        contador_ceros +=  1

        diferencia_suma_y_resta = numero_total_resta - numero_total_suma

        print(numero_total_suma , numero_total_resta , contador_ceros , diferencia_suma_y_resta , cantidad_numero_resta , cantidad_numero_suma)


                
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
