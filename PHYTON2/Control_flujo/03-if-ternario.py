#operador ternadio sentencia de control
edad = input("Ingresa tu edad ")# se solicita al usuario ingresar su edad
edad = int(edad)# se convierte en entero el valor solicitado

mensaje = "Es mayor" if edad >= 17 else "Es menor"

print(mensaje)