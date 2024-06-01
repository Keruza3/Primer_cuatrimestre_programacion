import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: 
apellido:
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = prompt("Ej 8 for" , "Ingrese el numero deseado")
        numero_ingresado = int(numero_ingresado)
        
        contador_3 = 0
        contador_2 = 0
        for contador in range(1 , numero_ingresado+1):
            contador_3 = 0
            for _ in range(1, contador+1):
                if contador % _ == 0:
                    contador_3 += 1
            if contador_3 < 3:
                    contador_2+= 1
                    print(contador)
        mensaje = f"Hay un total de {contador_2} numeros primos entr el 1 y {numero_ingresado}"
        print(mensaje)

        
        
        #alert("Ej 8" , f"""Los numeros primos entre el 1 y el {numero_ingresado} son: {contador}""")
                    
                        
                  
                   
              
                
            
             
                
               
                        
                       



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()