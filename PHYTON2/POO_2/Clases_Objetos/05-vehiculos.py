
#Definimos la clase Vehiculo
class Vehiculo:
    
    #Inicializamos las Variables `marca` y `modelo`
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo 
    #Metodo descripción    
    def descripcion(self):
        print(f"La marca del Vehiculo es {self.marca} y el modelo es {self.modelo}")

#Instanciamos la clase `Vehiculo`
vehiculo = Vehiculo("Mazda X3", "2023")
vehiculo.descripcion()   