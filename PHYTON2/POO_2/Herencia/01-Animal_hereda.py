class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass
    
    def __str__(self):
        # Este método se llama automáticamente cuando se usa print en una instancia de Animal
        return f"Soy un {self.__class__.__name__.lower()} y hago {self.hacer_sonido()}"

class Gato(Animal):
    def hacer_sonido(self):
        return "miau"
    
class Perro(Animal):
    def hacer_sonido(self):
        return "guaf"
    
class Loro(Animal):
    def hacer_sonido(self):
        return "quiere cacao"
    
class Vaca(Animal):
    def hacer_sonido(self):
        return "muuu"

# Crear instancias y probar
mi_gato = Gato("Whiskers")
print(mi_gato)  # Salida: Soy un gato y hago miau

mi_perro = Perro("Bucky")
print(mi_perro)  # Salida: Soy un perro y hago guaf

mi_loro = Loro("Pedro")
print(mi_loro)  # Salida: Soy un loro y hago quiere cacao

mi_vaca = Vaca("Paquita")
print(mi_vaca)  # Salida: Soy una vaca y hago muuu
