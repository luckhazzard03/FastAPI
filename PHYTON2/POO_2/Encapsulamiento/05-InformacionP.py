# Autor: Angel Medina
# Fecha: 03/09/2024
# Clases, objetos y Encapsulamiento

# Descripción: Crea una clase Persona que encapsule la información personal de una 
# persona, como nombre y edad.

# Requisitos:

# Define atributos privados para el nombre y la edad.
# Proporciona métodos públicos para establecer y obtener el nombre y la edad.
# Asegúrate de que la edad sea un número positivo y el nombre no esté vacío.


#Definición de la clase `Persona`
class Persona:
    def __init__(self, nombre, edad):
        
        self.__nombre = nombre
        self.__edad = edad
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre
    
    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("Edad debe ser positiva.")
            
    def get_edad(self):
        return self.__edad
    
    
# Crear una instancia de la clase `Persona`
persona = Persona("Angel Medina", 38)

#Obtener y mostrar la información
print(persona.get_nombre()) # Angel Medina
print(persona.get_edad())   # 38

#Modificar la edad
persona.set_edad(31)
print(persona.get_edad()) #31

#Modificar la edad
persona.set_edad(-5) # edad debe ser positiva