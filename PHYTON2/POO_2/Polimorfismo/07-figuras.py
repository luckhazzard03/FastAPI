# Autor: Angel Medina
# Fecha: 02/09/2024
# Polimorfismo con Interfaces Abstractas


# Clase Abstracta CalculadorDeAngulo:

# Define una interfaz abstracta para calcular ángulos. Contiene un método abstracto calcular_angulo que debe ser implementado por las clases derivadas.
# Clases Derivadas:

# SenoInverso: Implementa el cálculo del ángulo usando la función seno inverso.
# CosenoInverso: Implementa el cálculo del ángulo usando la función coseno inverso.
# TangenteInversa: Implementa el cálculo del ángulo usando la función tangente inversa.
# Función imprimir_angulo:

# Acepta un objeto que implementa la interfaz CalculadorDeAngulo, llama al método calcular_angulo, y luego imprime el ángulo en radianes y grados.
# Ejemplo de Uso:

# Crea instancias de las clases derivadas con valores de lados específicos.
# Llama a la función imprimir_angulo para mostrar los resultados calculados por cada tipo de calculador.
# Este enfoque utiliza el polimorfismo al tratar diferentes métodos de cálculo de ángulos de manera uniforme a través de una interfaz común. Cada clase derivada implementa el método calcular_angulo según su propia lógica, permitiendo que el código principal trabaje con objetos de diferentes tipos sin preocuparse por los detalles de implementación específicos.

from abc import ABC, abstractmethod
import math

# Definimos la clase abstracta `Calculadora_De_Angulo`
class Calculadora_De_Angulo(ABC):
    """
    Clase abstracta que define la interfaz para calcular ángulos en un triángulo.
    """
    @abstractmethod
    def calcular_angulo(self):
        """
        Método abstracto que debe ser implementado por las clases derivadas.
        Debe calcular y devolver el ángulo en radianes y grados.
        """
        pass

# Clase que implementa el cálculo del ángulo usando el seno inverso (arcsen)
class SenoInverso(Calculadora_De_Angulo):
    def __init__(self, a, c):
        """
        Inicializa una instancia de `SenoInverso`.
        :param a: Longitud del lado opuesto al ángulo.
        :param c: Longitud de la hipotenusa.
        """
        self.a = a
        self.c = c
    
    def calcular_angulo(self):
        """
        Calcula el ángulo usando la función seno inverso (arcsen).
        :return: Ángulo en radianes y grados.
        """
        angulo_rad = math.asin(self.a / self.c) # Calcula el ángulo en radianes
        angulo_deg = math.degrees(angulo_rad)   # Convierte el ángulo a grados
        return angulo_rad, angulo_deg

# Clase que implementa el cálculo del ángulo usando el coseno inverso (arccos)
class CosenoInverso(Calculadora_De_Angulo):
    def __init__(self, b, c):
        """
        Inicializa una instancia de `CosenoInverso`.
        :param b: Longitud del lado adyacente al ángulo.
        :param c: Longitud de la hipotenusa.
        """
        self.b = b # Lado adyacente
        self.c = c # Hipotenusa
        
    def calcular_angulo(self):
        """
        Calcula el ángulo usando la función coseno inverso (arccos).
        :return: Ángulo en radianes y grados.
        """
        angulo_rad = math.acos(self.b / self.c) # Calcula el ángulo en radianes
        angulo_deg = math.degrees(angulo_rad)   # Convierte el ángulo a grados
        return angulo_rad, angulo_deg

# Clase que implementa el cálculo del ángulo usando la tangente inversa (arctan)
class TangenteInversa(Calculadora_De_Angulo):
    def __init__(self, a, b):
        """
        Inicializa una instancia de `TangenteInversa`.
        :param a: Longitud del lado opuesto al ángulo.
        :param b: Longitud del lado adyacente al ángulo.
        """
        self.a = a # Lado opuesto
        self.b = b # Lado adyacente

    def calcular_angulo(self):
        """
        Calcula el ángulo usando la función tangente inversa (arctan).
        :return: Ángulo en radianes y grados.
        """
        angulo_rad = math.atan(self.a / self.b) # Calcula el ángulo en radianes
        angulo_deg = math.degrees(angulo_rad)   # Convierte el ángulo a grados
        return angulo_rad, angulo_deg

def imprimir_angulo(calculador: Calculadora_De_Angulo):
    """
    Imprime el ángulo calculado por un objeto que implementa la interfaz `Calculadora_De_Angulo`.
    :param calculador: Instancia de una clase derivada de `Calculadora_De_Angulo`.
    """
    angulo_rad, angulo_deg = calculador.calcular_angulo() # Llama al método `calcular_angulo` del objeto
    print(f"Ángulo: {angulo_rad:.4f} radianes ({angulo_deg:.2f} grados)") # Imprime el ángulo

if __name__ == "__main__":
    # Longitudes de los lados
    a = 3 # Lado opuesto
    b = 4 # Lado adyacente
    c = math.sqrt(a**2 + b**2) # Hipotenusa calculada usando la relación pitagórica (5 en este caso)
    
    # Crear instancias de las clases derivadas
    seno_calculador = SenoInverso(a, c)        # Instancia de `SenoInverso`
    coseno_calculador = CosenoInverso(b, c)    # Instancia de `CosenoInverso`
    tangente_calculador = TangenteInversa(a, b) # Instancia de `TangenteInversa`
    
    # Imprimir los ángulos calculados usando cada tipo de calculador
    print("Ángulo usando seno inverso:")
    imprimir_angulo(seno_calculador)
    
    print("\nÁngulo usando coseno inverso:")
    imprimir_angulo(coseno_calculador)
    
    print("\nÁngulo usando tangente inversa:")
    imprimir_angulo(tangente_calculador)
