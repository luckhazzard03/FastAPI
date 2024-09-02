# Autor: Angel Medina
# Fecha: 02/08/2024
# Clases, objetos, Herencia y Polimorfismo

# Descripción General
# Este ejercicio tiene como objetivo demostrar el uso de clases, herencia y polimorfismo en Python a través de un sistema que representa diferentes tipos de aves y sus dietas. Se implementa una jerarquía de clases para modelar aves y se utiliza polimorfismo para mostrar cómo cada tipo de ave tiene una dieta específica, aunque todas las clases derivadas comparten una interfaz común.

# Objetivo
# Crear un sistema orientado a objetos que represente diferentes tipos de aves con sus dietas específicas. El sistema debe utilizar herencia para extender una clase base común y polimorfismo para manejar las dietas de diferentes tipos de aves de manera uniforme.

# Instrucciones
# Definición de la Clase Base Ave:

# Crear una clase base Ave que tenga un constructor para inicializar los atributos mamiferos, peces y aves, que representarán las categorías generales de alimentos que puede consumir un ave.
# Implementar un método dieta que debe ser sobrescrito por las clases derivadas.
# Implementar un método __str__ para proporcionar una representación en cadena de la dieta general de las aves.
# Definición de Clases Derivadas:

# Clase Aguila:
# Hereda de Ave.
# Implementa el método dieta para devolver una cadena que describe la dieta específica del águila.
# Clase Halcon:
# Hereda de Ave.
# Añade un atributo adicional insectos para representar otro tipo de alimento específico para el halcón.
# Sobrescribe el método dieta para proporcionar una cadena que describa la dieta del halcón.
# Sobrescribe el método __str__ para incluir información sobre los insectos en la representación en cadena.
# Clase Condor:
# Hereda de Ave.
# Implementa el método dieta para devolver una cadena que describe la dieta específica del cóndor.
# Creación y Manejo de Objetos:

# Crear una lista de objetos que contenga instancias de Aguila, Halcon y Condor.
# Cada instancia debe ser inicializada con datos adecuados que representan sus dietas y alimentos preferidos.
# Iterar sobre la lista de objetos y llamar al método dieta para imprimir la dieta específica de cada ave.
# También imprimir la representación en cadena de cada objeto para mostrar la información completa sobre sus dietas.

# Requisitos
# Herencia: Utiliza herencia para extender la funcionalidad de la clase base Ave.
# Polimorfismo: Demuestra el polimorfismo al tratar diferentes tipos de aves de manera uniforme a través de la lista de objetos.
# Métodos Especiales: Implementa los métodos __init__, dieta y __str__ de manera adecuada en cada clase.


# Definimos la clase base `Ave`
class Ave:
    
    def __init__(self, mamiferos, peces, aves):
        #Constructor para inicializar los atributos
        self.mamiferos = mamiferos
        self.peces = peces
        self.aves =aves
    # Método que debe ser implementado por las clases derivadas
    def dieta(self):
        pass # Método vacío, se espera que las clases derivadas lo sobrescriban
    #Métpodo para obtener la representación en cadena del objeto
    def __str__(self):
        return(f"Esta es la dieta: {self.mamiferos} , {self.peces}, {self.aves}")
        
# Definimos la clase `Aguila`, que hereda de `Ave`
class Aguila(Ave):
    # Implementación específica del método `dieta` para `Aguila`
    def dieta(self):
        return "El águila come: Mámiferos, aves y peces"

# Definimos la clase `Halcon`, que hereda de `Ave`
class Halcon(Ave):
    
    def __init__(self, mamiferos, peces, aves, insectos):
        super().__init__(mamiferos, peces, aves)
        #Atributo especifico de `Halcon`
        self.insectos = insectos
    # Implementación específica del método `dieta` para `Halcon`
    def dieta(self):
        return "El Halcón come: Aves, mamíferos e insectos"
    
    def __str__(self):
        return (super().__str__() + f", e insectos: {self.insectos}")

# Definimos la clase `Condor`, que hereda de `Ave`
class Condor(Ave):
    # Implementación específica del método `dieta` para `Condor`
    def dieta(self):
        return "El cóndor come: Carroña de animales muertos"

# Crear una lista de objetos de tipo `Ave`
aves1 = [Aguila("ratas", "truchas", "gorriones"), 
         Halcon("ratones", "salmón", "pájaros", "moscas"), 
         Condor("cercas", "ganado", "osos")]

# Iterar sobre la lista de `aves`
for ave in aves1:
    # Llamar al método `dieta` para cada objeto `ave` y imprimir el resultado
    print(ave.dieta())
    # Imprimir la representación en cadena del objeto
    print(ave)