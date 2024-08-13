#"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error."""

n1 = float(input("Ingresa el Dividendo:  "))
n2 = float(input("Ingresa el Divisor:  "))

if n1 == 0 or n2 == 0:
    print("no se puede dividir por cero ")

else:
    print(n1/n2)