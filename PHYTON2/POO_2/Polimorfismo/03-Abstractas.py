# Autor: Angel Medina
# Fecha: 02/09/2024
# Polimorfismo con Interfaces Abstractas


# Ejercicio 3: Polimorfismo con Interfaces Abstractas
# Descripción:

# Usa clases abstractas para definir una interfaz común para diferentes tipos de figuras geométricas. Crea una clase abstracta Figura con un método abstracto area. Luego, implementa las clases Cuadrado y Circulo, cada una con su propia implementación del método area.

# Pasos:

# Importa ABC y abstractmethod de abc para definir clases abstractas y métodos abstractos.
# Crea la clase abstracta Figura con un método abstracto area.
# Implementa las clases Cuadrado y Circulo que hereden de Figura y definan el método area.
# Crea una función imprimir_area que acepte una instancia de Figura y llame a area.


from abc import ABC, abstractmethod
import math


#Definimos la clase `Figura`
class Figura(ABC):
    @abstractmethod    
    def area(self):
        pass# Este método abstracto debe ser implementado por todas las subclases
    
class Cuadrado(Figura):
    #Se inicializan la variable `lado`
    def __init__(self, lado):
        self.lado = lado
        
    
    def area(self):
        # Implementación del método area para un cuadrado
        return self.lado * self.lado
    
# Definimos la clase `Circulo` que también hereda de `Figura`
class Circulo(Figura):
    
    def __init__(self, radio):
        # Constructor que inicializa la variable `radio`
        self.radio = radio
        
    def area(self):
        # Implementación del método area para un círculo
        return math.pi * self.radio * self.radio
# Función que imprime el área de cualquier figura   
def imprimir_area(figura):
    # Esta función demuestra el polimorfismo,
    # ya que puede trabajar con cualquier objeto que herede de Figura
    print(f"Área: {figura.area()}")
    
    
    
#Ceación de la instancia de la clase `Cuadrado`
cuadrado = Cuadrado(4)

#Creación de la instancia de la clase ` Circulo`
circulo = Circulo(5)

# Llamamos a la función `mover_vehiculo` pasando la instancia `cuadrado`
imprimir_area(cuadrado)

# Llamamos a la función `mover_vehiculo` pasando la instancia `circulo`
imprimir_area(circulo)
    
        
