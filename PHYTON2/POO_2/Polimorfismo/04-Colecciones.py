# Autor: Angel Medina
# Fecha: 02/09/2024
# Polimorfismo con Colecciones de Objetos

# Ejercicio 4: Polimorfismo con Colecciones de Objetos
# Descripción:

# Crea una lista de diferentes tipos de animales, cada uno con un método hacer_sonido. Usa polimorfismo para hacer que cada animal haga su sonido correspondiente.

# Pasos:

# Crea una clase base Animal con un método hacer_sonido.
# Crea clases derivadas Perro y Gato con implementaciones específicas del método hacer_sonido.
# Crea una lista de objetos Animal, añadiendo instancias de Perro y Gato.
# Itera sobre la lista y llama al método hacer_sonido para cada animal.

#Definimos la clase `Animal`
class Animal:
    
    def hacer_sonido(self):
        pass # Método que  debe ser implementado por las clases derivadas
    
class Perro(Animal):
    def hacer_sonido(self):
        return "El perro dice Guaf!!"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "El gato hace Miau!"
    
class Loro(Animal):
    def hacer_sonido(self):
        return "El loro dice QUIERE CACAO!"

animales = [Perro(), Gato(), Loro()]

for animal in animales:
    print(animal.hacer_sonido())