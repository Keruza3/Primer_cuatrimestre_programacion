import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Ignacio 
apellido: Ullua
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        
        lamparas = self.combobox_cantidad.get()

        lamparas = int(lamparas)    

        marca = self.combobox_marca.get()


        if lamparas >= 6:
            
            descuento = 50

            # caso b
            if lamparas == 5:
                 if marca == "ArgentinaLuz":
                    
                    descuento = 40

                 else:
                     
                     descuento = 30 
            
            # caso c
            if lamparas == 4:
                
                if marca == "ArgentinaLuz" or  marca == "FelipeLamparas":

                        descuento = 25
                else:
                    
                        descuento = 20

            
            #caso d
                    
            if lamparas == 3:
                
                    if marca == "ArgentinaLuz":
                    
                        descuento = 10
                    else:
                
                        if marca == "FelipeLamparas":
                        
                            descuento = 10
                        else:

                            descuento = 5
        else:
            descuento = 0

        importe_lamparas_precio = lamparas * 800
        importe_lamparas_descuento = (importe_lamparas_precio * descuento) / 100
        descuento_final = importe_lamparas_precio - importe_lamparas_descuento
          #caso e            
        if descuento_final >= 4000:
                
                descuento = 5
                importe_lamparas_descuento = (importe_lamparas_precio * descuento) / 100
                descuento_final = importe_lamparas_precio - importe_lamparas_descuento
            

        mensaje =  f"""El precio final de porducto es de: 
                                    cantidad: {lamparas}
                                    Precio: ${importe_lamparas_precio}
                                    Descuento: {descuento}%
                                    Cantidad descuento: ${importe_lamparas_descuento}
                                    ---------------------------------
                                    Precio final: ${descuento_final}"""

        alert ("TP if Iluminacion" , mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()