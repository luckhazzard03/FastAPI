# Autor: Angel Eduardo Medina
# Fecha: 28/08/2024
# Este algoritmo muestra el tipo de moto, incluyendo la marca, el modelo y el cilindraje,
# mediante la definición de una clase, la implementación de sus métodos y la creación de un objeto.

# Definimos la clase Moto
class Moto:
    # Inicializamos las variables `marca` y `modelo`
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Definimos el método `cilindraje` que muestra el cilindraje de la moto
    def cilindraje(self):
        print(f"La moto es de marca {self.marca}, modelo {self.modelo}, con cilindraje: 180 cc")

# Creamos el objeto `mi_moto` de la clase `Moto`
mi_moto = Moto("Akt", 2017)  # Se crea una instancia de la clase `Moto` y se asigna a la variable `mi_moto`
mi_moto.cilindraje()         # Salida esperada: La moto es de marca Akt, modelo 2017, con cilindraje: 180 cc
