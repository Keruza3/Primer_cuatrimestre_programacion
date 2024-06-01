"""
Alumno: Juan Ignacio Ullua
Divicion: 114
Ejercicio: 
"""



"""
El tipo (validar "barbijo", "jabón" o "alcohol")
El precio: (validar entre 100 y 300)
La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
La marca y el Fabricante.
  
 Se debe informar lo siguiente:
Del más caro de los barbijos, la cantidad de unidades y el fabricante.
Del ingreso con más unidades, el fabricante.
Cuántas unidades de jabones hay en total.
"""


bandera_barbijo = True
barbijo_precio_maximo = 0
barbijo_cantidad = 0
marca_mayor_barbijo = ""
bandera_unidad = True
unidad_maxima = 0
fabricante_unidad_maxima = ""
jabones_totales = 0
jabon = 0



for _ in range (5):
    producto = input("Ingrese el producto: ")

    while producto != "barbijo" and producto != "jabon" and producto!= "alcohol":

        producto = input("Ingrese el producto: ")

    precio = input("Ingrese el precio del producto: ")

    precio = float(precio)

    while  100 < precio and precio > 300:

        precio = input("Ingrese el precio del producto: ")
        precio = float(precio)

    unidades = input("Ingrese la cantitad del producto: ")
    unidades = int(unidades)
    while  0 <= unidades and unidades > 1000:

        unidades = input("Ingrese la cantitad del producto: ")
        unidades = int(unidades)
    marca = input("Ingrese su marca: ")

 #parte del punto A
    match producto:
        case "barbijo":
            barbijo_precio = precio

        case "jabon":
            jabon = unidades

 #punto C 
    jabones_totales += jabon
            

#punto A

if bandera_barbijo == True:
    barbijo_precio_maximo = barbijo_precio
    barbijo_cantidad = unidades
    marca_mayor_barbijo = marca
    bandera_barbijo = False
else:
    if barbijo_precio > barbijo_precio_maximo:
        barbijo_precio_maximo = barbijo_precio
        barbijo_cantidad = unidades
        marca_mayor_barbijo = marca

#punto B

if bandera_unidad == True:
    unidad_maxima = unidades
    fabricante_unidad_maxima = marca
    bandera_unidad = False
else:
    if unidades > unidad_maxima:
        unidad_maxima = unidades
        fabricante_unidad_maxima = marca

print (f"""El mas caro de los barbijos tiene una cantidad de: {barbijo_cantidad} unidades y es fabricado por: {marca_mayor_barbijo}
El item con mas unidades es: {fabricante_unidad_maxima} y es: {unidad_maxima}
La cantidad de jabones es: {jabones_totales}
Gracias por usar el programa""")








    
