# # # # Autor: Angel Medina
# # # # Fecha: 02/09/2024
# # #Herencia, Encapsulamiento, Abstracción, composición y interfaces

# Sistema de Pagos
# Enunciado:
# Desarrolla un sistema de pagos que permita procesar pagos usando diferentes métodos
# (por ejemplo, tarjeta de crédito, PayPal y transferencia bancaria). Utiliza polimorfismo
# para definir un método común procesar_pago() en cada tipo de método de pago.

# Pasos:
# Define una clase base abstracta MetodoDePago con un método abstracto procesar_pago().
# Crea clases derivadas TarjetaDeCredito, PayPal y TransferenciaBancaria, cada una implementando
# el método procesar_pago() de manera específica.
# Escribe una función realizar_pago() que tome un objeto de tipo MetodoDePago y llame al método 
# procesar_pago().
# # En el bloque principal, crea instancias de TarjetaDeCredito, PayPal y TransferenciaBancaria,

from abc import ABC, abstractmethod


class MetodoDePago(ABC):
    @abstractmethod
    def procesar_pago(self):
        pass
    
class TarjetaDeCredito(MetodoDePago):
    def __init__(self, numero_tarjeta, monto):
        self.numero_tarjeta = numero_tarjeta
        self.monto = monto
        
    def procesar_pago(self):
        return f"Procesando pago: {self.monto} con la tarjeta de credito No: {self.numero_tarjeta}"
    
class PayPal(MetodoDePago):
    def __init__(self, cuenta_paypal, monto):
        self.cuenta_paypal = cuenta_paypal
        self.monto = monto   
        
    def procesar_pago(self):
        return f"Procesando pago: {self.monto} con la cuenta de PayPal No: {self.cuenta_paypal}"
    
class TransferenciaBancaria(MetodoDePago):
    def __init__(self, cuentaBancaria, monto):
        self.cuentaBancaria = cuentaBancaria
        self.monto = monto
        
    def procesar_pago(self):
        return f"Procesando pago: {self.monto} con la cuenta bancaria No: {self.cuentaBancaria}"
    
    
def realizar_pago(pago: MetodoDePago):
    print(pago.procesar_pago())
    
    
if __name__ == "__main__":
    
    pagos_procesados = [TarjetaDeCredito("1234-5678-9876-5432", 100),
                        PayPal("usuario@paypal.com", 50),
                        TransferenciaBancaria("1234567890", 200)]
    
    for pagos in pagos_procesados:
        realizar_pago(pagos)
    

