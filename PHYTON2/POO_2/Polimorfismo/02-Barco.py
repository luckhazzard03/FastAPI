# Autor: Angel Medina
# Fecha: 02/09/2024
# Polimorfismo con Herencia y Sobrescritura

# Descripción:

# Extiende el ejercicio anterior agregando una nueva clase Barco que también herede de Vehiculo. Sobrescribe el método mover para que describa cómo se mueve un barco.

# Pasos:

# Agrega la clase Barco con su propia implementación del método mover.
# Modifica el código para incluir un objeto de tipo Barco y llama a mover_vehiculo con él.


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
    
# Definimos la clase `Barco`, que hereda de `Vehiculo`
class Barco(Vehiculo):
    # Sobrescribimos el método `mover` de la clase base
    def mover(self):
        return "El barco esta navegando por el agua"

# Función que acepta un objeto de tipo `Vehiculo` y llama a su método `mover`
def mover_vehiculo(vehiculo):
    # Llama al método `mover` del objeto `vehiculo` y imprime el resultado
    print(vehiculo.mover())

# Creación de una instancia de la clase `Coche`
coche = Coche()
# Creación de una instancia de la clase `Bicicleta`
bicicleta = Bicicleta()
# Creación de una instancia de la clase `Barco`
barco = Barco()

# Llamamos a la función `mover_vehiculo` pasando la instancia `coche`
mover_vehiculo(coche)      # Output: El coche está conduciendo por la carretera.

# Llamamos a la función `mover_vehiculo` pasando la instancia `bicicleta`
mover_vehiculo(bicicleta)  # Output: La bicicleta va por el sendero.

# Llamamos a la función `mover_vehiculo` pasando la instancia `barco`
mover_vehiculo(barco)# Output: El barco está navegando por el agua.
    
    
