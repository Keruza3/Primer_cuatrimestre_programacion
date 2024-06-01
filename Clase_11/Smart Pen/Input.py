from Validate import validate_numer, validate_length


def get_int(mensaje: str, mensaje_error: str, minimo:int, maximo: int, intentos:int) -> int | None:
    """se pide un numero entero, este se comprueba  si cumple los requisitos ingresados mediante la funcion validate_number

    Args:
        -mensaje (str): se ingresa el mensaje que se le quiere dar al usuario
        -mensaje_error (str): El mensaje error que se da si lo ingresado no cumple con los requisitos dados
        -minimo (int): El numero minimo entero que debe ingresar el usuario
        -maximo (int): El numero maximo entero que debe ingresar el usuario
        -intentos (int): La cantidad de intentos que se le da al usuario para responder

    Returns:
        int | None: Puede devolver el mismo numero si cumple con lo pedido, en el caso de que no no se devuelve un
    """
    
    numero_entero = int(input(mensaje))

    numero_entero = validate_numer(mensaje_error, numero_entero, minimo, maximo, "int", intentos)

    if numero_entero == None:

        print(mensaje_error)

        return None
    
    else:
        
        return numero_entero
    




def get_float(mensaje: str, mensaje_error: str, minimo:float, maximo: float, intentos:int) -> float | None:

    numero_flotante = input(mensaje)

    numero_flotante = float(numero_flotante)

    numero_flotante = validate_numer(mensaje_error, numero_flotante, minimo, maximo, "float", intentos)

    if numero_flotante == None:
        
        return None

    else:
        
        return numero_flotante
    


def get_string(texto: str) -> str:
    
    cadena = input(texto)

    cadena = validate_length

    if cadena == None:
        
        return None
    
    else:
        
        return cadena