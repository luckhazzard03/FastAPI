#Objetivo: Añadir métodos adicionales a una clase para manejar más atributos.
#Instrucciones:
#Define una clase   Motor con los atributos cilindraje, piston, y tipo_Vehiculo.
#Implementa un método especificaciones que imprima la información sobre la cilindraje, el pistón, y el tipo de vehiculo.
#Agrega un método actualizar_procesador que permita actualizar el valor del atributo cilindraje.
#Crea una instancia de la clase Motor, muestra sus especificaciones, actualiza el procesador, y vuelve a mostrar las especificaciones.


# Se define la clase `motor`
class Motor:
    
    def __init__(self, cilindraje, piston, tipo_Vehiculo):
        self.cilindraje = cilindraje
        self.piston = piston
        self.tipo_Vehiculo = tipo_Vehiculo
        
    def especificaciones(self):
        print(f"El motor es de cilindraje {self.cilindraje}, de piston {self.piston} y sirve para tipo de vehiculo {self.tipo_Vehiculo}") 
        
    def actualizar_cilindraje(self, nuevo_cilindraje):
        self.cilindraje = nuevo_cilindraje

#Crear una instancia y  mostrar las especificaciones
_mi_motor = Motor(250, "monocilindrico", "moto")
_mi_motor.especificaciones() # Salida esperada: El motor es de cilindraje 250, de pistones monocilindrico y sirve para tipo de vehiculo moto

# Actualizar cilindraje y mostrar especificaciones
_mi_motor.actualizar_cilindraje(300)
_mi_motor.especificaciones() # Salida esperada:El motor es de cilindraje 300, de pistones monocilindrico y sirve para tipo de vehiculo moto