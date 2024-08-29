#Autor: Angel Medina
#fecha: 19/08/2024
#clases objetos y Herencia 

#se define la clase `Musico` a Heredar 
class Musico:
    def __init__(self, nombre):
        # Inicializa el objeto Musico con un nombre
        self.nombre = nombre
        
    def genero_musica(self):
        # Método que debería ser sobreescrito por las subclases
        # Para proporcionar el género musical específico del músico
        pass
    
    def __str__(self):
        # Método especial que se llama automáticamente cuando se usa print en una instancia de Musico
        # Construye una cadena que describe al músico, su nombre, su tipo y el género musical que toca
        return f"Hola, mi nombre es {self.nombre} y soy {self.__class__.__name__.lower()} y el género que toco es {self.genero_musica()}"

class Guitarrista(Musico):
    def genero_musica(self):
        # Implementa el género musical específico para un Guitarrista
        return "Hardcore"
    
class Baterista(Musico):
    def genero_musica(self):
        # Implementa el género musical específico para un Baterista
        return "Metalcore"
    
class Vocalista(Musico):
    def genero_musica(self):
        # Implementa el género musical específico para un Vocalista
        return "Hardcore"

# Crear instancia de la clase Guitarrista
guitarrista = Guitarrista("Eduardo")
print(guitarrista)  # Salida esperada: Hola, mi nombre es Eduardo y soy guitarrista y el género que toco es Hardcore

# Crear instancia de la clase Baterista
baterista = Baterista("Angel")
print(baterista)  # Salida esperada: Hola, mi nombre es Angel y soy baterista y el género que toco es Metalcore

# Crear instancia de la clase Vocalista
vocalista = Vocalista("Sergio")
print(vocalista)  # Salida esperada: Hola, mi nombre es Sergio y soy vocalista y el género que toco es Hardcore
