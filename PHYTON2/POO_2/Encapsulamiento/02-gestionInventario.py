# Autor: Angel Medina
# Fecha: 30/08/2024
# Clases, objetos y Encapsulamiento

#Crea una clase llamada Producto que represente un producto en un inventario.

#Definicion de la clase `Producto`
class Producto:
    # Método constructor para inicializar una instancia de la clase
    def __init__(self, nombre, precio, cantidad):
        # Atributo privado que almacena el nombre del producto
        self.__nombre = nombre   # Atributo privado (no debe ser accedido directamente desde fuera de la clase) "Encapsula" 
        self.__precio = precio    # Atributo privado (no debe ser accedido directamente desde fuera de la clase) "Encapsula"
        self.__cantidad = cantidad   # Atributo privado (no debe ser accedido directamente desde fuera de la clase) "Encapsula" 
    
    
    def establecer_precio(self, precio):
        if precio > 0: 
            self.__precio = precio
        else: 
            print("El precio debe ser un numero entero")
            
    def aumentar_cantidad(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("La cantidad a añadir debe ser positiva.")
            
    def disminuir_cantidad(self, cantidad):
        if cantidad > 0 and cantidad <= self.__cantidad:
            self.__cantidad -= cantidad
        else:
            print("La cantidad a restar debe ser positiva y no puede exceder la cantidad disponible.")
            
    def obtener_info(self):
        return (f"Nombre { self.__nombre}, Precio{self.__precio:.2f}, Cantidad: {self.__cantidad}")


#Creación de la instancia de la clase `Producto`
producto = Producto("Impresora", 2200.00, 10)
producto.establecer_precio(1100.00)
producto.aumentar_cantidad(5)
producto.disminuir_cantidad(3)


#Obtención y visualización del producto 
print(producto.obtener_info())