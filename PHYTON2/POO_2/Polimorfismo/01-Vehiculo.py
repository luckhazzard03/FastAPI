# Autor: Angel Medina
# Fecha: 02/09/2024
# Polimorfismo con Herencia y Sobrescritura

# Crea una jerarquía de clases que represente diferentes tipos de vehículos. Todos los vehículos tienen un método mover, pero cada tipo de vehículo lo implementa de manera diferente.

# Pasos:

# Crea una clase base llamada Vehiculo con un método mover.
# Crea dos clases derivadas, Coche y Bicicleta, que hereden de Vehiculo. Implementa el método mover en cada clase de manera específica.
# Crea una función mover_vehiculo que acepte un objeto de tipo Vehiculo y llame a su método mover.
# Crea instancias de Coche y Bicicleta y usa la función mover_vehiculo para llamar al método mover en ambos objetos.


# Definimos la clase base `Vehiculo`
class Vehiculo:
    # Método que  debe ser implementado por las clases derivadas
    def mover(self):
        pass

# Definimos la clase `Coche`, que hereda de `Vehiculo`
class Coche(Vehiculo):
    # Sobrescribimos el método `mover` de la clase base
    def mover(self):
        return "El coche está conduciendo por la carretera"

# Definimos la clase `Bicicleta`, que hereda de `Vehiculo`
class Bicicleta(Vehiculo):
    # Sobrescribimos el método `mover` de la clase base
    def mover(self):
        return "La bicicleta va por el sendero"

# Función que acepta un objeto de tipo `Vehiculo` y llama a su método `mover`
def mover_vehiculo(vehiculo):
    # Llama al método `mover` del objeto `vehiculo` y imprime el resultado
    print(vehiculo.mover())

# Creación de una instancia de la clase `Coche`
coche = Coche()
# Creación de una instancia de la clase `Bicicleta`
bicicleta = Bicicleta()

# Llamamos a la función `mover_vehiculo` pasando la instancia `coche`
mover_vehiculo(coche)      # Output: El coche está conduciendo por la carretera.

# Llamamos a la función `mover_vehiculo` pasando la instancia `bicicleta`
mover_vehiculo(bicicleta)  # Output: La bicicleta va por el sendero.
