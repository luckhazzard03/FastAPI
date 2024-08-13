#"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales
# o superiores a 1000 $ mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos
# mensuales y muestre por pantalla si el usuario tiene que tributar o no."""

edad = int(input("Ingresa tu edad:  "))
ingresos = int(input("Cuales son tus Ingresos mensuales:  "))


if edad >= 20 and ingresos >= 1000:
    print("Tiene que pagar impuesto: ")

    
else: 
    if edad < 20:
        print("tu edad es menor a lo solicitado por lo tanto no tributas", edad)
    if ingresos < 1000:
        print("tus ingresos son menores  a lo solicitado por lo tanto no tributas", ingresos)