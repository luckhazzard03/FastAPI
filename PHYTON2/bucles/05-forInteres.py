#"""Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión."""

invertir = int(input("Cúal es la cantidad a invertir: "))
interes = int(input("Cúal es el interes porcentual: "))
year = int(input("Años: "))

for i in range(year):
    invertir *= 1 + interes / 100 
    print("Capital trascurrido " + str(i+1) + " años: " + str(round(invertir, 2)))
    