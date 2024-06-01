import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Ignacio
apellido: Ullua
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


   
    def btn_validar_on_click(self):
        
        bandera_estado_civil = False
        
        apellido = prompt("apellido" , "Ingrese su apellido:")
        
        while apellido == "":
                
                apellido = prompt("apellido" , "Ingrese su apellido:")
                
                
        while apellido == None:
            
            apellido = prompt("apellido" , "Ingrese su apellido:")
            
        
        edad = prompt("Edad" , "Ingrese su edad:")

        while edad == "" or edad == None:
            
             edad = prompt("Edad" , "Ingrese su edad:")
        
        edad = int(edad)

        while edad <18 or edad >90:
            
            edad = prompt("Edad" , "Ingrese su edad entre un rango de 18 y 90 años")

            edad = int(edad)

        
        while not bandera_estado_civil:
            estado_civil = prompt("Estado civil", "Ingrese su estado civil:")

            if estado_civil == "" or estado_civil is None:
                continue

            estado_civil = estado_civil.lower()

            match estado_civil:
                case "soltero" | "soltera" | "casado" | "casada" | "divorciado" | "divorciada" | "viudo" | "viuda":
                    bandera_estado_civil = True

                case _:
                
                    continue
                 
            
                
            numero_de_legajo = prompt("Legajo" , "Ingrese su numero de legajo:")

            while numero_de_legajo == "" or numero_de_legajo == None:
                continue

            numero_de_legajo = int(numero_de_legajo)

            while numero_de_legajo <= 1000 or numero_de_legajo >=9999:

                numero_de_legajo = prompt("Legajo" , "Ingrese su numero de legajo: (Tiene que ser de 4 cifras y sin 0 al principio)")

                numero_de_legajo = int(numero_de_legajo)

        
        self.txt_apellido.delete(0 , customtkinter.END)
        self.txt_edad.delete(0 , customtkinter.END)
        self.txt_legajo.delete(0 , customtkinter.END)
        
        self.txt_apellido.insert(0 , apellido)
        self.txt_edad.insert(0 , edad)
        self.combobox_tipo.set(estado_civil)
        self.txt_legajo.insert(0 , numero_de_legajo)
 
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
