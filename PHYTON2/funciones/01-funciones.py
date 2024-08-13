# estos son funciones con parametros funcionales 
def hola(nombre, apellido="Aslam"):#PARAMETROS
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")#uso de sus parametros de la función {nombre}
    
#por defecto toma el argumento del apellido    
hola("Angel", " Medina")# llama a la función "Angel" es el ARGUMENTOS
#en este caso toma el parametro que le estamos indicando al apellido 
hola("Bucky")# llama a la función "ARGUMENTOS" 



hola(apellido="Medina", nombre="Emmanuel")
