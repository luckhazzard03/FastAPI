#Autor:Angel Eduardo Medina
#Fecha: 28/08/2024
#En este algoritmo se pretende mostrar que genero toca el musico,
# instrumento y rol o tipo de especialidad

# Se define la clase Musico
class Musico:
    
    # Inicializamos las variables `tipo` y `instrumento`
    def __init__(self, tipo, instrumento):
        self.tipo = tipo
        self.instrumento = instrumento
    
    # Se define la varible `genero`
    @classmethod
    def genero(cls, tipo):
        # Crea una instancia usando el valor predeterminado para `instrumento`
        return cls(tipo, instrumento='Guitarra')
    
    # Se define la Varieble  `role_musico`
    def roles_musico (self):
        print(f"El musico es de {self.tipo}, toca el {self.instrumento} y su rol es de sesión")
    
# Usar el método de fábrica para crear un músico con tipo 'Jazz'
musico = Musico.genero("Jazz")
musico.roles_musico()   # Salida esperada: El músico es de Jazz, toca el Guitarra y su rol es de sesión