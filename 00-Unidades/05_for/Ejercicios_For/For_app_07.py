import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("Ej 7 for" , "Ingrese un numero")
        bandera_primo = False
        numero = int(numero)

        for _ in range(numero):
            if numero % 2 == 0:
                bandera_primo = True
                break
        if bandera_primo == False:
            alert("ej 7 for" , "El numero es primo")
        else:
            alert("ej 7 for" , "El numero no es primo")


        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()