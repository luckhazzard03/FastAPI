#"""Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
# Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta
# de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los 
# descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta."""


def aplicar_descuento(precio, descuento):
    return precio - (precio * descuento / 100)  

def aplicar_IVA(precio, porcentaje):
    return  precio + (precio * porcentaje / 100 )


#cesta Es un dicccionario 
#funcion toma los parametros 
#"""Inicialización de total: Se inicializa una variable total con el valor 0.
#Esta variable se utilizará para acumular el resultado de aplicar la función
# funcion' a cada precio de la cesta."""
def cesta_precio(cesta, funcion):
    total = 0
    for precio, descuento in cesta.items():
        total += funcion(precio, descuento)
    return total

# Calcular el precio tras aplicar descuentos
precio_con_descuentos = cesta_precio({1000: 20, 500: 10, 100: 1}, aplicar_descuento)
print('El precio de  la compra tras aplicar los descuentos es: ', precio_con_descuentos)

# Calcular el precio tras aplicar el IVA
precio_con_IVA = cesta_precio({1000: 20, 500: 10, 100: 1}, aplicar_IVA)
print('El precio de  la compra tras aplicar el IVA es: ',precio_con_IVA)
