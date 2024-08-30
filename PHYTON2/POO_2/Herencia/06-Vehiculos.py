# Autor: Angel Medina
# Fecha: 19/08/2024
# Clases, objetos y Herencia 

# Se define la clase base `Vehiculo`, que servirá como clase padre
class Vehiculo:
    def __init__(self, marca, modelo, año):
        # Constructor para inicializar los atributos básicos de un vehículo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    # Método para arrancar el vehículo
    def arrancar(self):
        return "Arrancando el vehículo"
    
    # Método para detener el vehículo
    def detener(self):
        return "Deteniendo el vehículo"
    
    # Método para obtener una representación en cadena del objeto
    def __str__(self):
        return  (f"{self.marca} {self.modelo} ({self.año}): {self.arrancar()} y {self.detener()}")

# Se define la clase `Coche`, que hereda de `Vehiculo`
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas):
        # Llamada al constructor de la clase base `Vehiculo`
        super().__init__(marca, modelo, año)
        # Atributo específico de `Coche`
        self.numero_puertas = numero_puertas
        
    # Método para abrir las puertas del coche
    def abrir_puertas(self):
        return f"Abrir {self.numero_puertas} puertas"
    
    # Método sobreescrito para arrancar el coche (modifica el comportamiento de la clase base)
    def arrancar(self):
        return "Arrancando el Coche"
    
    # Método para obtener una representación en cadena del objeto, extendiendo la clase base
    def __str__(self):
        return (super().__str__() + f", {self.abrir_puertas()}")

# Se define la clase `Motocicleta`, que hereda de `Vehiculo`
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_escapamento):
        # Llamada al constructor de la clase base `Vehiculo`
        super().__init__(marca, modelo, año)
        # Atributo específico de `Motocicleta`
        self.tipo_escapamento = tipo_escapamento
    
    # Método para realizar un wheelie (una maniobra con la motocicleta)
    def hacer_wheelie(self):
        return "Haciendo wheelie"
    
    # Método sobreescrito para arrancar la motocicleta (modifica el comportamiento de la clase base)
    def arrancar(self):
        return "Arrancando la motocicleta"
    
    # Método para obtener una representación en cadena del objeto, extendiendo la clase base
    def __str__(self):
        return (super().__str__() + f", Tipo de escape: {self.tipo_escapamento}, {self.hacer_wheelie()}")

# Se crea una instancia de la clase `Coche`
coche = Coche("Mazda", "X3", 2023, 4)  # Nota: corregido `DEPORTIVO` a 4, ya que `numero_puertas` debe ser un número entero
    
# Se crea una instancia de la clase `Motocicleta`
motocicleta = Motocicleta("Honda", "CBR600", 2023, "Deportivo")
    
# Se imprime la información del coche y la motocicleta
print(coche)
print(motocicleta)
