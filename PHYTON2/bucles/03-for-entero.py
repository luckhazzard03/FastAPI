#"""
# Escribir un programa que pida al usuario un número entero positivo y muestre 
# por pantalla todos los números impares desde 1 hasta ese número separados por 
# comas."""

numero = int(input("ingrese el número:"))

for i in range(1,numero+1,2):
    print(i, end=",")

