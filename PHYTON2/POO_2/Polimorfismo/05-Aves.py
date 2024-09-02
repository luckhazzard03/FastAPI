# Autor: Angel Medina
# Fecha: 02/09/2024
# Polimorfismo con Colecciones de Objetos

# Ejercicio 4: Polimorfismo con Colecciones de Objetos
# Descripción:
# Crea una lista de diferentes tipos de Aves, cada uno con un método dieta.
# Usa polimorfismo para hacer que cada ave muestre cual es su dieta correspondiente.

# Pasos:
# Crea una clase base Ave con un método dieta.
# Crea clases derivadas Águila, Halcón y Condor con implementaciones específicas del método dieta.
# Crea una lista de objetos Ave, añadiendo instancias de Águila, Halcón y Cóndor.
# Itera sobre la lista y llama al método dieta para cada Ave.

# Definimos la clase base `Ave`
class Ave:
    # Método que debe ser implementado por las clases derivadas
    def dieta(self):
        pass # Método vacío, se espera que las clases derivadas lo sobrescriban

# Definimos la clase `Aguila`, que hereda de `Ave`
class Aguila(Ave):
    # Implementación específica del método `dieta` para `Aguila`
    def dieta(self):
        return "El águila come: Mámiferos, aves y peces"

# Definimos la clase `Halcon`, que hereda de `Ave`
class Halcon(Ave):
    # Implementación específica del método `dieta` para `Halcon`
    def dieta(self):
        return "El Halcón come: Aves, insectos y pequeños mamíferos"

# Definimos la clase `Condor`, que hereda de `Ave`
class Condor(Ave):
    # Implementación específica del método `dieta` para `Condor`
    def dieta(self):
        return "El cóndor come: Carroña de animales muertos"

# Crear una lista de objetos de tipo `Ave`
aves = [Aguila(), Halcon(), Condor()]

# Iterar sobre la lista de `aves`
for ave in aves:
    # Llamar al método `dieta` para cada objeto `ave` y imprimir el resultado
    print(ave.dieta())
