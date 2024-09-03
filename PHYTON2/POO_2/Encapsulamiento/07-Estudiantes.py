# # Autor: Angel Medina
# # Fecha: 03/09/2024
# # Clases, objetos y Encapsulamiento

# Registro de Estudiantes
# Descripción: Crea una clase Estudiante que gestione la información de un estudiante.

# Requisitos:

# Define atributos privados para el nombre del estudiante, la matrícula, y las calificaciones.
# Proporciona métodos públicos para obtener el nombre y la matrícula del estudiante.
# Implementa un método para añadir una calificación y otro para obtener el promedio de calificaciones.
# Asegúrate de que solo se puedan añadir calificaciones entre 0 y 10.

#Definimos la clase `Estudiante`
class Estudiante:
    def __init__(self, nombre, matricula, calificaciones=None):
        
        self.__nombre = nombre
        self.__matricula = matricula
        # Si calificaciones no se proporciona, se inicializa como una lista vacia
        self.__calificaciones = calificaciones if calificaciones is not None else[]
        
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_matricula(self):
        return self.__matricula
    
    def agregar_calificacion(self, calificacion):
        if 0 <= calificacion <= 10:
            self.__calificaciones.append(calificacion)
        else:
            print("Calificación debe estar entre 0 y 10. ")
            
    def obtener_promedio(self):
        if self.__calificaciones:
            return sum(self.__calificaciones) / len(self.__calificaciones)
        else:
            return 0
    
    def __str__(self):
        return (f"Alumno: {self.__nombre}\nMatricula: {self.__matricula}\nCalificaciones: {self.__calificaciones}\nPromedio: {self.obtener_promedio():.2f} ")
    
    
#Se crea la instancia de la clase `Estudiante`
estudiante = Estudiante("Emmanuel", 10223)

#Obtener y mostrar la información usando el método __str__
print(estudiante) #Esto invoca automáticamente estudiante.__str__()

#Agregar calificaciones
estudiante.agregar_calificacion(5)
estudiante.agregar_calificacion(7)
estudiante.agregar_calificacion(8)

#Mostrar la información despues de agregar las calificaciones 
print(estudiante) #  Esto invoca automáticamente estudiante.__str__()