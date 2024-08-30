# Autor: Angel Medina
# Fecha: 19/08/2024
# Clases, objetos y Herencia 

# Diseña una jerarquía de clases para representar diferentes formas geométricas.
# Crea una clase base llamada Forma y dos clases derivadas: Circulo y Rectangulo.
#Crea instancias de cada tipo de forma y muestra su área y perímetro usando el método __str__().

#se importa la libreria `math`
import math

# Se define la clase `Forma`
class Forma:
    #Método constructor `calcular_area`
    def calcular_area(self):
        pass
    
    #Método constructor `calcular_perimetro`
    def calcular_perimetro(self):
        pass
    
        

#se define la clase`Circulo` derivada de `Forma`
class Circulo(Forma):
    #Método constructor para Inicializar los atributos 
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        return math.pi * self.radio ** 2 #Formula para calcular el área del circulo 
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio #Formula para calcular el perímetro del circulo 

    # Método para obtener una representación en cadena del objeto con detalles de los cálculos
    def __str__(self):
        return (f"Circulo con radio {self.calcular_area()} y perímetro {self.calcular_perimetro()}")
# se define la clase `Rectangulo` derivada de la clase `Forma`
class Rectangulo(Forma):
    # Método constructor para inicializar los atributos 
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    #Método para `calcular_area`
    def calcular_area(self):
        return  self.ancho * self.alto
    
    #Método para `calcular_perimetro`
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)
    
    # Método para obtener una representación en cadena del objeto con detalles de los cálculos
    def __str__(self):
        return (f"Rectángulo con área {self.calcular_area()} y perímetro {self.calcular_perimetro()}")
        
    
# Se crea las instancias de las clases `Circulo` y `Rectangulo`
circulo = Circulo(5)
rectangulo = Rectangulo (5, 6)

print(circulo)
print(rectangulo)