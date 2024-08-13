#"""Escribir un programa que pida al usuario un número entero y muestre
# por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# """


# numero = int(input("Introduce la altura del triángulo (entero positivo): "))


# for i in range(numero):
#     for j in range(i+1):
#         print("*", end="")
#     print("")

# for i in range(numero, -1, -1):
#     for j in range(i+1):        
#         print("*", end="")
#     print("")
    
numero = int(input("Introduce la altura del rombo (entero positivo): "))

# Parte superior del rombo
for i in range(numero):
    # Imprime espacios en blanco para alinear a la derecha
    for j in range(numero - i - 1):
        print(" ", end="")
    # Imprime asteriscos en forma de pirámide hacia arriba
    for j in range(i + 1):
        print("* ", end="")
    print("")

# Parte inferior del rombo
for i in range(numero - 2, -1, -1):  # Comienza desde numero-2 hasta 0 (excluyendo el 0)
    # Imprime espacios en blanco para alinear a la derecha
    for j in range(numero - i - 1):
        print(" ", end="")
    # Imprime asteriscos en forma de pirámide hacia abajo
    for j in range(i + 1):
        print("* ", end="")
    print("")


    
        

