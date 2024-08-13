print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi, div, potencia, porcentaje")

resultado = ""

while True:
    if not resultado:
        resultado = input("ingrese el número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresar operación: ")
    if op.lower() == "salir":
        break
    n2= input("Ingrese siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    elif op.lower() == "potencia":
        resultado **= n2
    elif op.lower() == "porcentaje":
        resultado =n2 *(resultado/100)
    else:
        print("operación no valida ") 
        break
    
    print(f"El resultado es {resultado}")