#"""Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
# titular (que es una persona) y cantidad (puede tener decimales).
# El titular será obligatorio y la cantidad es opcional. Construye 
# los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. 
# El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos. """

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        return f"Cuenta\nTitular: {self.__titular} - Cantidad: {self.__cantidad}"
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad



if __name__ == "__main__":
    # Crear una cuenta con titular "Juan" y cantidad inicial 100
    cuenta = Cuenta("Juan", 100)
    
    # Mostrar la cuenta
    print(cuenta.mostrar())
    
    # Ingresar 50 a la cuenta
    cuenta.ingresar(50)
    print(cuenta.mostrar())
    
    # Retirar 30 de la cuenta
    cuenta.retirar(30)
    print(cuenta.mostrar())
