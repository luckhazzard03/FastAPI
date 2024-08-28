# definimos la clase Casa
class Casa:
    def __init__ (self, tipo, color):
        self.tipo = tipo
        self.color = color 
        
    @classmethod
    def crear_casa_arquitectura(cls, color):
        return cls(tipo = "apartamento", color =color)
    #definimos el metodo `descripcion`
    def descripcion(self):
        print(f"La casa es de tipo {self.tipo} y el color {self.color}")
        
#Instanciamos la clase `Casa`
casa = Casa.crear_casa_arquitectura("Azul")
casa.descripcion()    # Salida esperada: La casa es de tipo Montaña y color Rojo     
    