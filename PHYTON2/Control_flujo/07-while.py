#ciclo while 
# numero = 1
# while numero < 100:# lo primero que hace es evaluar el while si es que es verdadero nos permite ejecutar la operación "numero *=2"
#     print(numero)
#     numero *=2

# loops While
comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)
    
    
#LOOPS INFINITOS 
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() != "salir":
        break
    



