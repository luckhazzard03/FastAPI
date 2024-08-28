# Se define la clase Perro 
class Perro:
    #se inicializan las variables "nombre" y "edad"
    # __init__ es el metodo constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # se inicializa la variable     
    def ladrar(self):
        print(f"{self.nombre} tiene {self.edad} años y dice Guau!")
        
        
#Crear un objeto
mi_perro = Perro("Aslam", 3) #  se crea la instancia de la clase `Perro` y asignandola a la Variable `mi_perro`
mi_perro.ladrar() # Salida: Aslam dice: Guau!