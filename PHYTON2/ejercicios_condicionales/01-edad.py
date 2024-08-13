#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Ingresa tu edad "))

#las evaluciones de sentencias de control se manejan de arriba hacia abajo de mayor a menor
# si es mayor de 17 Es mayor de edad
if edad > 17:
    print("Eres mayor de Edad")

#sino es menor de edad  
else:
    print("Eres menor de edad")