# Autor: Angel Medina
# Fecha: 19/08/2024
# Clases, objetos y Herencia

# Se define la clase `Animal` a Heredar
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def hacer_sonido(self):
        pass
    
    def __str__(self):
        return (f"El nombre del animal es {self.nombre} y su edad es {self.edad} años, "
                f"el sonido que hace es {self.hacer_sonido()}")

class Mamifero(Animal):
    def amamantar(self):
        return "Amamantado"
    
    def hacer_sonido(self):
        return "Sonido de mamífero"
    
class Ave(Animal):
    def volar(self):
        return "Volando"
    
    def hacer_sonido(self):
        return "Sonido de ave"
    
# Crear instancias y mostrar información    
mamifero = Mamifero("Tigre", 6)
ave = Ave("Águila", 7)

# Imprimir información de las instancias
print(mamifero)
print(ave)
