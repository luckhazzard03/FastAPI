#crear una variable
# #recibe el mensaje que le queremos entregar al ususario "input()"
n1 = input("Ingrese el primer numero ")
n2 = input("Ingrese el segundo numero ")

n1 = int(n1)
n2= int(n2)

suma = n1 + n2      
resta = n1 - n2
mult = n1 * n2
div = n1 / n2
pote = n1 ** n2      #potenciación
porce = n1 * n2 / 100 #operador de porcentaje

mensaje = f"""
Para los números {n1} y {n2},
el resultado de la Suma es {suma}.
el resultado de la Resta es {resta}.
el resultado de la Multiplicación es {mult}.
el resultado de la División es {div}.
el resultado de la Potenciación es {pote}.
el resultado del Porcentaje es {porce}.
"""

print(mensaje) 