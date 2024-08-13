#"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
# nombre posterior a la N y el grupo B por el resto. Escribir un programa que 
# pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""

nombre = input("¿Cuál es tu nombre?: ")
sexo = input("¿Cuál es tu sexo? (M o F): ")

nombre_minusculas = nombre.lower()  # Convertir el nombre a minúsculas para comparaciones

if sexo == "F":
    if nombre_minusculas < "m":
        grupo = "A"
    else:
        grupo = "B"
elif sexo == "M":
    if nombre_minusculas > "n":
        grupo = "A"
    else:
        grupo = "B"
else:
    grupo = "B"  # Si el sexo no es ni "M" ni "F", se asigna al grupo B

print("Tu grupo es " + grupo)
