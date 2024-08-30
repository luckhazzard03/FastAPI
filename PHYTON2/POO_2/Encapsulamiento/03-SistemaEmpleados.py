# Autor: Angel Medina
# Fecha: 30/08/2024
# Clases, objetos y Encapsulamiento

#Desarrolla una clase llamada Empleado para gestionar información de empleados
# en una empresa.
#Atributos:
#__nombre (privado): El nombre del empleado.
#__edad (privado): La edad del empleado.
#__salario (privado): El salario del empleado.
#Métodos:

#__init__(self, nombre, edad, salario): Constructor que inicializa los atributos.
#establecer_salario(self, salario): Método para establecer el salario del empleado. Debe validar que el salario sea un número positivo.
#cumplir_anios(self): Método para aumentar la edad del empleado en 1 año.
#aumento_salario(self, porcentaje): Método para aumentar el salario del empleado en un porcentaje. Debe validar que el porcentaje sea positivo.
#mostrar_info(self): Método que devuelve una cadena con la información del empleado, incluyendo el nombre, edad y salario.
#Objetivo: El acceso a los atributos privados debe estar restringido, y los métodos deben controlar cómo se modifica la información del empleado.

#Definición de la clase `Empleados`
class Empleados:
    
    def __init__(self, nombre, edad, salario):
        
        self.__nombre = nombre
        self.__edad = edad
        self.__salario = salario
     
    #  Método para establecer el salario del empleado.  
    def establecer_salario(self, salario):
        if salario > 0:
            self.__salario = salario
        else:
            print("El salario debe ser un numero positivo")
            
    #Método para aumentar la edad del empleado en 1 año.       
    def cumplir_years(self):
        self.__edad += 1  
    
    # Método para aumentar el salario del empleado en un porcentaje.   
    def aumento_salario(self, porcentaje):
        if porcentaje > 0:
            self.__salario += self.__salario * (porcentaje / 100)
        else:
            print ("El porcentaje debe ser positivo")
     
     
    # Método que devuelve una cadena con la información del empleado   
    def mostrar_info(self):
        return (f"El nombre es: {self.__nombre}, su edad es: {self.__edad} y salario: {self.__salario:.2f}")
    
    
    
#Creación de la instancia de la clase `Empleados`
empleado = Empleados("Carlos Andres", 26, 90000.00)
empleado.establecer_salario(92000.00)
empleado.cumplir_years()
empleado.aumento_salario(20)

#Obtención y visualización de los Empleados 
print(empleado.mostrar_info())