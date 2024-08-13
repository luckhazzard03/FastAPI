# definimos las variables " parametros"
def suma(a, b):
    resultado = a + b
    return resultado# retorna al resultado

c = suma(1, 2) # se  crea nuevo "c" parametro y le pasamos los argumentos 
d = suma(c, 2) # se  crea nuevo "d" parametro y le pasamos los argumentos

print(d) # se imprime popr pantalla el resuldao sería 5