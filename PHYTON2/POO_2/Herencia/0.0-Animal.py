#Definimos la clase `Animal`

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
    
class Perro(Animal):
    def hacer_sonido(self):
        return "Guaf"
    
class Loro(Animal):
    def hacer_sonido(self):
        return "Quiere cacao"
    
class Vaca(Animal):
    def hacer_sonido(self):
        return "Muuu"

mi_gato = Gato("Whiskers")
print(mi_gato.hacer_sonido())  # Salida: Miau

mi_perro = Perro("Bucky")
print(mi_perro.hacer_sonido())


mi_loro = Loro("Pedro")
print(mi_loro.hacer_sonido())


mi_vaca = Vaca("Paquita")
print(mi_vaca.hacer_sonido())