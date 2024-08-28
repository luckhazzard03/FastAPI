# Autor: Angel Eduardo Medina
# Fecha: 28/08/2024
# Este algoritmo define una clase `Torno` que representa un torno con atributos para el tipo y el mecanizado.
# Incluye un método de clase para crear instancias con un valor predeterminado para el mecanizado,
# y un método para mostrar la información del torno.

# Definimos la clase Torno
class Torno:
    
    # El método __init__ inicializa una nueva instancia de la clase `Torno`.
    # Recibe `tipo` y `mecanizado` como parámetros para establecer los atributos correspondientes.
    def __init__(self, tipo, mecanizado):
        self.tipo = tipo
        self.mecanizado = mecanizado
        
    # El método de clase `corte` crea una instancia de `Torno` con un valor predeterminado para `mecanizado`.
    # Se utiliza para simplificar la creación de objetos con un mecanizado fijo ('valvulas').
    @classmethod
    def corte(cls, tipo):
        return cls(tipo, mecanizado='valvulas')
    
    # El método `material` imprime la información del torno, incluyendo el tipo, el mecanizado y el material.
    def material(self):
        print(f"El torno es de tipo {self.tipo}, mecaniza {self.mecanizado} y el material es de Bronce.")

# Usamos el método de clase `corte` para crear una instancia de `Torno` con el tipo 'Revolver' y mecanizado 'valvulas'.
torno = Torno.corte("Revolver")

# Llamamos al método `material` para mostrar la información del torno.
torno.material()  # Salida esperada: El torno es de tipo Revolver, mecaniza valvulas y el material es de Bronce.
