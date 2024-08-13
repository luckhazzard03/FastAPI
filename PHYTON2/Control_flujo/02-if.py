edad = input("Ingresa tu edad ")# se solicita al usuario ingresar su edad
edad = int(edad)# se convierte en entero el valor solicitado

#las evaluciones de sentencias de control se manejan de arriba hacia abajo de mayor a menor
# si es mayor de 54 tiene descuento 
if edad > 54:
    print("Puede ver la pelicula con descuento")
#sentencia de control si es mayor de edad puede ingresar a ver la pelicula 
elif edad > 17:
    print("Puedes ver la pelicula")
#si es menor de edad no puede ingresar 
else:
    print("No puedes entrar, eres menor de edad")
    
