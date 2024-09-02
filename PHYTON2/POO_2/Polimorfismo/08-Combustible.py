# # Autor: Angel Medina
# # Fecha: 02/09/2024

#  Vehículos y Combustible
# Descripción: Crea una jerarquía de clases para representar diferentes tipos de vehículos: Vehiculo, Coche, Motocicleta, y Camion. Implementa un método consumo_combustible() en la clase base Vehiculo que debe ser sobrescrito por cada clase derivada para calcular el consumo de combustible específico del vehículo.

# Pasos:

# Define una clase base Vehiculo con un método abstracto consumo_combustible().
# Crea clases derivadas Coche, Motocicleta, y Camion, cada una con su propia implementación del método consumo_combustible().
# Crea una lista de objetos de tipo Vehiculo que contenga instancias de Coche, Motocicleta, y Camion.
# Itera sobre la lista y llama al método consumo_combustible() para cada objeto, mostrando el consumo de combustible de cada vehículo.

from abc import ABC, abstractmethod

# Definimos una clase abstracta `Vehiculos` que actúa como la clase base
class Vehiculos(ABC):
    @abstractmethod
    def consumo_combustible(self):
        """
        Método abstracto que debe ser implementado por las clases derivadas.
        No tiene implementación en la clase base y se espera que cada clase derivada
        proporcione su propia implementación.
        """
        pass
    
# Definimos la clase `Coche` que hereda de `Vehiculos`
class Coche(Vehiculos):
    def __init__(self, litros_km):
        """
        Constructor para inicializar el atributo `litros_km`, que representa el consumo
        de combustible del coche en litros por kilómetro.
        """
        self.litros_km = litros_km
        
    def consumo_combustible(self):
        """
        Implementación específica del método `consumo_combustible` para la clase `Coche`.
        Retorna una cadena que describe el consumo de combustible del coche.
        """
        return f"Consumo de combustible del coche es {self.litros_km} litros/km"
    
# Definimos la clase `Moto` que hereda de `Vehiculos`
class Moto(Vehiculos):
    def __init__(self, litros_km):
        """
        Constructor para inicializar el atributo `litros_km`, que representa el consumo
        de combustible de la moto en litros por kilómetro.
        """
        self.litros_km = litros_km
        
    def consumo_combustible(self):
        """
        Implementación específica del método `consumo_combustible` para la clase `Moto`.
        Retorna una cadena que describe el consumo de combustible de la moto.
        """
        return f"Consumo de combustible de la moto es: {self.litros_km} litros/km"
    
# Definimos la clase `Camion` que hereda de `Vehiculos`
class Camion(Vehiculos):
    def __init__(self, litros_km):
        """
        Constructor para inicializar el atributo `litros_km`, que representa el consumo
        de combustible del camión en litros por kilómetro.
        """
        self.litros_km = litros_km
        
    def consumo_combustible(self):
        """
        Implementación específica del método `consumo_combustible` para la clase `Camion`.
        Retorna una cadena que describe el consumo de combustible del camión.
        """
        return f"Consumo de combustible del Camion es: {self.litros_km} litros/km"
    
# Función que acepta un objeto de tipo `Vehiculos` y muestra el consumo de combustible
def mostrar_consumo(vh: Vehiculos):
    """
    Imprime el consumo de combustible del vehículo proporcionado.
    """
    print(vh.consumo_combustible())
    
# Bloque principal que se ejecuta cuando el script se ejecuta directamente
if __name__ == "__main__":
    # Crear una lista de objetos de tipo `Vehiculos`, cada uno con un tipo diferente de vehículo
    vehiculos = [Coche(0.08), Moto(0.05), Camion(0.15)]
    
    # Iterar sobre la lista de vehículos e imprimir el consumo de combustible de cada uno
    for vehiculo in vehiculos:
        mostrar_consumo(vehiculo)
