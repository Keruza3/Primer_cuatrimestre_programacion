class Alumno:

    especie = "Humana"  #Atributo de clase
                        # si se le cambia el atributo se le cambia a todo     

    def __init__(self, nombre: str, apellido: str, DNI: int):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        

    def presentarse(self, mensaje_final:str):
        
        return f"Hola mi nombre es: {self.nombre} mi apellido es: {self.apellido} {mensaje_final} y mi especie es: {self.especie}"
    


alumno_01 = Alumno("Juan", "ullua", "123123123")

print(alumno_01.presentarse("chau"))

print(alumno_01.especie)