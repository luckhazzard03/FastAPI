# # Autor: Angel Medina
# # Fecha: 03/09/2024
# # Clases, objetos y Encapsulamiento

#  Gestión de un Inventario de Productos
# Descripción: Crea una clase Producto que gestione la información de un producto en un inventario.

# Requisitos:

# Define atributos privados para el nombre del producto, el código de producto, y el stock.
# Proporciona métodos públicos para obtener el nombre y el código del producto.
# Implementa un método para actualizar el stock, asegurándote de que no se pueda tener un stock negativo.
# Añade un método para agregar stock y otro para reducir stock.


#Definición de la clase `Producto`
class Producto:
    #Se  inicializan las variables `nombre`, `codigo` `stock`
    def __init__(self, nombre, codigo, stock):
        
        self.__nombre = nombre  #Se encapsulan el atributo `nombre`
        self.__codigo = codigo  #Se encapsula el atributo `codigo`
        self.__stock = stock    #Se encapsula el atributo `stock`
        
    #Método para obtener el nombre del producto    
    def obtener_nombre(self):
        return self.__nombre 
    #metodo para obtener el codigo de la laptop
    def obtener_codigo(self):
        return self.__codigo
    #Método para Agregar al stock
    def agregar_stock(self, cantidad):
        if cantidad > 0:
            self.__stock += cantidad
        else:
            print("Cantidada a agregar debe ser positiva. ")
    #Método para reducir el stock        
    def reducir_stock(self, cantidad):
        if 0 <= cantidad <= self.__stock:
            self.__stock -= cantidad
        else:
            print(f"Cantidad no válida o stock insuficiente. Intentaste reducir {cantidad} pero el stock actual es {self.__stock}.")
    #Método para obtener el stock       
    def obtener_stock(self):
        return self.__stock
    
    def __str__(self):
        return (f"Producto: {self.__nombre}\nCodigo: {self.__codigo}\ncantidad: {self.__stock}")   
#se crea la intancia de la clase `Producta`
producto = Producto("Laptop", "LT123", 10)


# Obtener y mostrar la información usando el método __str__
print(producto)  # Esto invoca automáticamente producto.__str__()

# Modificar el stock
producto.agregar_stock(20)
print(producto)  # Verifica el estado después de agregar stock

# Reducir stock
producto.reducir_stock(5)
print(producto)  # Verifica el estado después de reducir stock

# Intentar reducir el stock a una cantidad inválida
producto.reducir_stock(20)  # Esto imprimirá el mensaje de error
print(producto)  # Verifica el estado después del intento fallido de reducción