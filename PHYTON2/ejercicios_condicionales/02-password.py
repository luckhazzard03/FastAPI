#"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""

key = "contraseña 123"
password = input("Ingresa tu contraseña:  ")

if key.lower() == password.lower():
    print("tu contraseña es correcta ")
    
else:
    print("la contraseña no coincide")