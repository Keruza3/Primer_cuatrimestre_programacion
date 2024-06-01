import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Juan Ignacio
apellido: ullua
---
Ejercicio dojo 3
(if match)


La empresa spaceX , nos contrata para poder hacer el cálculo de precio final y descuentos para un viaje al espacio exterior
el costo por millón de kilómetros es de 8 bitcoin 

podes viajar a Marte (60 millones de KM) , la Luna (½ millón de KM)y a Titan (1300 millones de KM)
podes elegir si viajar en verano, primavera  otoño o invierno.

para los viajes a Marte
Si viajan más de 5 personas te hacemos un 50 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 10% , en otoño y primavera se le suma un 25% al precio con descuento.

para los viajes la Luna 
si viajan más de 5 personas te hacemos un 40 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 15% ,  en otoño y primavera al precio con descuento se le suma un 25%

para los viajes a Titan
si viajan más de 5 personas te hacemos un 30 % de descuento sobre el precio,
viajando en verano al precio final se le suma un 10% , en otoño y primavera al precio con descuento se le suma un 20%

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Marte', 'La luna', 'Titan']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.label1 = customtkinter.CTkLabel(master=self, text="Personas")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_personas = customtkinter.CTkEntry(master=self)
        self.txt_personas.grid(row=0, column=1)
        
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self): 
         
         
        Costo_marte = 480
        Costo_luna = 4 
        Costo_titan = 10400 

        estaciones = self.combobox_estaciones.get()
        planetas = self.combobox_destino.get()
        personas = self.txt_personas.get()
        personas = int(personas)
        descuento = 1
        aumento_al_final = 1

        bandera_personas = False

        match planetas:
             case "Marte":
                if personas > 5:
                     descuento = 50
                     bandera_personas = True
                else:
                     match estaciones:
                          case "Primavera" | "Otoño":
                               if bandera_personas == True:
                                        descuento = 50
                                        aumento_al_final = 25


                          case "Verano":
                                if bandera_personas:
                                      descuento = 50
                                      aumento_al_final = 10
                          
                          case _:
                                        if bandera_personas == True:
                                                descuento = 50
             case "Luna":
                if personas > 5:
                        descuento = 40
                        bandera_personas == True
                        match estaciones:
                                case "Verano":
                                    if bandera_personas == True:
                                                descuento = 40
                                                aumento_al_final = 15
                                case "Otono" | "Primavera":
                                    if bandera_personas == True:
                                                descuento = 40
                                                aumento_al_final = 25
                                case _:
                                        if bandera_personas == True:
                                                descuento = 40
                                        
             case "Titan":
                 if personas > 5:
                      descuento = 30
                      bandera_personas = True
                      match estaciones:
                            case "Verano":
                                  if bandera_personas == True:
                                        descuento = 30
                                        aumento_al_final = 10

                            case "Otoño" | "Primavera":
                                 if bandera_personas == True:
                                        descuento = 30
                                        aumento_al_final = 20
                                

        precio_marte = Costo_marte * descuento / 100
        precio_marte = Costo_marte - precio_marte

        precio_marte_aumento = Costo_marte * aumento_al_final / 100
        precio_marte_aumento = precio_marte_aumento + precio_marte


        precio_luna = Costo_luna * descuento / 100
        precio_luna = Costo_luna - precio_luna

        precio_luna_aumento = Costo_luna * aumento_al_final / 100
        precio_luna_aumento = precio_luna_aumento + precio_luna

        precio_titan = Costo_titan * descuento / 100
        precio_titan = Costo_titan - precio_titan

        precio_titan_aumento = Costo_titan * aumento_al_final / 100
        precio_titan_aumento = precio_titan_aumento + precio_titan

        alert("Ejercicio dojo 3" , f"El final es de {precio_titan} + {precio_luna_aumento} + {precio_marte}")
                        


"""
para los viajes a Marte
Si viajan más de 5 personas te hacemos un 50 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 10% , en otoño y primavera se le suma un 25% al precio con descuento.

para los viajes la Luna 
si viajan más de 5 personas te hacemos un 40 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 15% ,  en otoño y primavera al precio con descuento se le suma un 25%

para los viajes a Titan
si viajan más de 5 personas te hacemos un 30 % de descuento sobre el precio,
viajando en verano al precio final se le suma un 10% , en otoño y primavera al precio con descuento se le suma un 20%

"""

                 


        
            
                
                

      
        
        
      
            
    
if __name__ == "__main__":
        app = App()
        app.geometry("300x300")
        app.mainloop()