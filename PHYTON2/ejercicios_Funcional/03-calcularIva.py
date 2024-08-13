#"""ESTE EJERCICIO PRETENDE MOSTRAR EL CALCULO DEL IVA DESCUENTO Y COSTE DE LAS BOLSAS DE CIERTOS 
#PRODUCTOS DE UNA TIENDA"""


def calcular_total(valor_producto, descuento, iva, bolsa):
    #Aplicar el descuento
    valor_con_descuento = valor_producto - (valor_producto * (descuento / 100))
    #Aplicar prcio con bolsa
    cantidad_bolsa = bolsa * 100
    #Aplicar iva 
    valor_final = valor_con_descuento + cantidad_bolsa +(valor_con_descuento * (iva/100))
    
    return valor_final

#solicitar al usuario que ingrese el valor del producto
valor_producto = float(input("Ingrese el valor del producto: "))
#Definir el porcentaje de descuento e IVA
descuento = float(input("Ingresa el porcentaje de descuento: "))
iva  = float(input("Ingresa el porcentaje del IVA: "))
#Definir la cantidad de bolsas
bolsa = float(input("ingrese la cantidad de bolsas: "))


#Calcular el total a pagar 
total = calcular_total(valor_producto, descuento, iva, bolsa)


#Mostrar el resultado
print(f"El total a pagar depués de aplicar un descuento de {descuento}% el IVA de {iva}% y la bolsa {bolsa} es: ${total:.2f}")


