#"""Este ejercicio nos permite ingresar el valor del producto calculando el descuento
# el iva y el total de todos los productos ingresados"""

def calcular_total(valor_producto, descuento, iva):
    # Aplicar el descuento
    valor_con_descuento = valor_producto - (valor_producto * (descuento / 100))
    # Aplicar el IVA
    valor_final = valor_con_descuento + (valor_con_descuento * (iva / 100))
    
    return valor_final

# Solicitar la cantidad de productos
cantidad_productos = int(input("¿Cuántos productos deseas procesar? "))

# Inicializar una variable para acumular el total de todos los productos
total_general = 0.0

for i in range(cantidad_productos):
    print(f"\nProducto {i + 1}")
    
    # Solicitar al Usuario que ingrese el valor del producto
    valor_producto = float(input("Ingrese el valor del producto: "))
    
    # Definir el porcentaje de descuento e IVA
    descuento = float(input("Ingresa el porcentaje de descuento: "))
    iva = float(input("Ingresa el porcentaje del IVA: "))
    
    # Calcular el total a pagar para el producto actual
    total_producto = calcular_total(valor_producto, descuento, iva)
    
    # Mostrar el resultado
    print(f"El total a pagar después de aplicar un descuento de {descuento}% y un IVA de {iva}% es: $ {total_producto:.2f}")
    
    # Acumular el total de este producto en el total general
    total_general += total_producto

# Mostrar el total general
print(f"\nEl total a pagar por todos los productos es: $ {total_general:.2f}")
