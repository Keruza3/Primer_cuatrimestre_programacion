import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

temperatura = 0
edad = 0 
contador = 0
contador_masculino = 0
contador_femenino = 0
contador_nb = 0 



while contador <5:
    
    contador += 1
    nombre = prompt("Ingresar nombre" , "ingrese su nombre")
    sexo = prompt ("Ingreso sexo" , "ingrese su sexo")
    temperatura = prompt("Ingreso temperatura" , "Ingrese su temperatura")
    temperatura = int(temperatura)
    
    match sexo:
        case "m":
            contador_masculino += 1
        case "f":
            contador_femenino +=1
        case "nb":
            contador_nb += 1
            

temperatura = prompt("Ingreso temperatura" , "Ingrese su nombre")




#cual es el sexo mas ingresado

if contador_masculino > contador_femenino:
    if contador_masculino > contador_nb:
        contador_mayor = f"El sexo mayor ingresado es masculino con {contador_masculino} personas"
        
else:
    if contador_femenino > contador_masculino:
        contador_femenino > contador_nb
        contador_mayor = f"El sexo mayor ingresado es femenino con {contador_femenino} personas"

if contador_nb > contador_masculino:
    contador_nb > contador_femenino
    contador_mayor = f"El sexo mayor ingresado es no binario con {contador_nb} personas"

print(contador_mayor)
    