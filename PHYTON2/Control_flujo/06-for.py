# loops for 
# nos muestra el rango de numeros en este caso sería de 0,1,2,3,4
for numero in range(5):# range(5) es un iterable
    print(numero, numero * 'Hola mundo ')
    
# CICLO FOR CON BREAK   
buscar = 5
for numero in range(6):# range(6) es un iterable
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break# rompe el ciclo 
    
# ciclo FOR ELSE    
buscar = 10
for numero in range(6):# range(6) es un iterable
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break# rompe el ciclo 
else:
    print("no encontrado")
    
# se utiliza para iterar en cada uno de los caracteres
for char in "Ultimate Python":
    print(char)