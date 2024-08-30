#Autor: Angel Medina
#fecha: 19/08/2024
#clases objetos y Herencia 

class Restaurante:
    def __init__(self, menu):
        self.menu = menu
        
        
    def desayuno(self):
        pass
    
    def almuerzo(self):
        pass
    
    def __str__(self):
        return (f"el menu de hoy es {self.menu} hace parte del plato {self.__class__.__name__.lower()}" 
               f", del desayuno {self.desayuno()} y del almuerzo {self.almuerzo()}")

class Corriente(Restaurante):
    def desayuno(self):
        return "Caldo de costilla"
    
    def almuerzo(self):
        return "Arroz con pollo"

class Ejecutivo(Restaurante):
    def desayuno(self):
        return "Moñona"
    
    def almuerzo(self):
        return "Bistec con papas"

class Especial(Restaurante):
    def desayuno(self):
        return "Caldo y moñona"
    
    def almuerzo(self):
        return "Ceviche de camarón"
    # crea instancia de la clase `Corriente`
corriente = Corriente("Caldo de costilla y huevos ")
print(corriente)