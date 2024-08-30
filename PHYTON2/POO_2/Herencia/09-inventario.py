# Autor: Angel Medina
# Fecha: 19/08/2024
# Clases, objetos y Herencia 


#Diseña una jerarquía de clases para representar productos en un inventario.
# Crea una clase base llamada Producto y dos clases derivadas: Electrodomestico
# y Ropa.

#se define la clase Padre `Producto`
class Producto:
    #Método constructor para inicializar los atributos
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return (f"Producto: {self.nombre}. Precio es:{self.precio}")

#Se define la clase `Electrodomestico` derivada de la clase Padre`Producto`
class Electrodomestico(Producto):
    #Método constructor para inicializar los atributos
    def __init__(self, nombre, precio, consumo_energia):
        super().__init__(nombre, precio)
        self.consumo_energia = consumo_energia
        
    
    def __str__(self):
        return super().__str__() + f". Consumo de energía: {self.consumo_energia}"
     
     
    
#Se define la clase `Ropa` derivada de la clase Padre`Producto`
class Ropa(Producto):
    #Método constructor para inicializar los atributos
    def __init__(self, nombre, precio, tamaño, material):
        super().__init__(nombre, precio)
        self.tamaño = tamaño
        self.material = material
    
    def __str__(self):
        return super().__str__() + f". Tamaño es {self.tamaño}. Material {self.material}"    
        
        
# se crea las instancias de las clases `Electrodomestico` y `Ropa`
electrodomestico = Electrodomestico("Nevera", 1000000, "A+")    
ropa = Ropa("Camiseta", 20000, "M", "Algodón")    

print(electrodomestico)
print(ropa)