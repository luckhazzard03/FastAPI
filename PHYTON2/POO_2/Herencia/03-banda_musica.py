#Autor: Angel Medina
#fecha: 19/08/2024
#clases objetos y Herencia 


class Bandas:
    def __init__(self, nombre_musico):
        self. nombre_musico = nombre_musico
        
        
    def genero_musica(self):
        pass
    
    def __str__(self):
        # Método que devuelve una representación en cadena de texto del objeto Bandas
        return f"Hola, soy {self.nombre_musico} de la Banda {self.__class__.__name__.lower()} y tocamos {self.genero_musica()}"
    
    
class Blink(Bandas):
    def genero_musica(self):
        return "Punk"
        
class Avenged(Bandas):
    def genero_musica(self):
        return "Hardcore"

class Chevelle(Bandas):
    def genero_musica(self):
        return "New metal"
    
class Benjamin(Bandas):
    def genero_musica(self):
        return "Hardcore"
    
    
# crea instancia de la clase `Blink`
blink = Blink("Travis Baker")
print(blink)

# crea instancia de la clase `Avenged`
avenged = Avenged("M.Shadows")
print(avenged)


# crea instancia de la clase `Chevelle`
chevelle = Chevelle("Peter Loeffler")
print(chevelle)


# crea instancia de la clase `Benjamin`
benjamin = Benjamin("Burnley")
print(benjamin)

