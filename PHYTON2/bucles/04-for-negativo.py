#"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la
# cuenta atrás desde ese número hasta cero separados por comas."""

numero = int(input("ingrese el número:"))

for i in range(numero, -1, -1):
    print(i, end=",")

