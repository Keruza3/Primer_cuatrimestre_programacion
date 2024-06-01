def validate_numer(mensaje_error:str ,numero:int, minimo: int | float, maximo:int | float , type , intentos) -> int | None:
    

    for _ in range(intentos):
    
        if numero < minimo or numero > maximo:
             
            numero = int(input(mensaje_error))

    if type == "int":
                
            numero = int(numero)

            return numero

    else:
                
        if type == "float":

                numero = float(numero)

                return numero

def validate_length(texto, mensaje_error, minimo, maximo, intenos):
    
    logitud = len(texto)

    for _ in range(intenos):
        
        if logitud < minimo or logitud <maximo:
            
            texto = input(mensaje_error)

            longitud = len(texto)

        else:
        
            return texto



