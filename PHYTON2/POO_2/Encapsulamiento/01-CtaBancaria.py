# Definición de la clase `CuentaBancaria`
class CuentaBancaria:
    # Método constructor para inicializar una instancia de la clase
    def __init__(self, saldo):
        # Atributo privado que almacena el saldo de la cuenta
        self.__saldo = saldo  # Atributo privado (no debe ser accedido directamente desde fuera de la clase) "Encapsula"
    
    # Método público para realizar un depósito en la cuenta
    def depositar(self, cantidad):
        # Verifica si la cantidad a depositar es positiva
        if cantidad > 0:
            # Si la cantidad es positiva, se suma al saldo "Encapsula"
            self.__saldo += cantidad
        # Si la cantidad es negativa o cero, no se realiza ningún depósito (se puede añadir lógica adicional para manejar este caso si se desea)
    
    # Método público para obtener el saldo actual de la cuenta
    def obtener_saldo(self):
        # Devuelve el saldo actual de la cuenta "Encapsula"
        return self.__saldo

# Creación de una instancia de `CuentaBancaria` con un saldo inicial de 1000
cuenta = CuentaBancaria(1000)

# Realización de un depósito de 500 en la cuenta
cuenta.depositar(500)

# Obtención y visualización del saldo actual de la cuenta (debería ser 1500 después del depósito)
print(cuenta.obtener_saldo())  # Salida: 1500
