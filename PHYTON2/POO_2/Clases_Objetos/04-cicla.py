# Definimos la clase Cicla
class Cicla:
    # Inicializamos las variables `Tipo` y `Deporte`
    def __init__(self, Tipo, Deporte):
        self.Tipo = Tipo
        self.Deporte = Deporte
     
    # Método de clase que crea una instancia de `Cicla` con un deporte predeterminado (`'BMX'`)
    @classmethod
    def crear_cicla_bmx(cls, Tipo):
        return cls(Tipo, Deporte='BMX')
    
    # Método de instancia que imprime la información sobre la cicla
    def ciclaBMX(self):
        print(f"La cicla es de tipo {self.Tipo} para el deporte de {self.Deporte}")
     
    # Método de clase que crea una instancia de `Cicla` con un deporte predeterminado (`'BMX'`)
    @classmethod
    def crear_cicla_montana(cls, Tipo):
        return cls(Tipo, Deporte='MONTAÑA') 
    
    # Método de instancia que imprime la información sobre la cicla
    def ciclaMONTANA(self):
        print(f"La cicla es de tipo {self.Tipo} para el deporte de {self.Deporte}")
    


#Creamos el objeto
# Usamos el método de clase `crear_cicla_bmx` para crear una instancia de `Cicla` con el tipo 'BMXC'
cicla = Cicla.crear_cicla_bmx("BMXC")

# Llamamos al método `ciclaBMX` para mostrar la información sobre la cicla
cicla.ciclaBMX()  # Salida esperada: La cicla es de tipo BMXC para el deporte de BMX

#Creamos el objeto
# Usamos el método de clase `crear_cicla_montana` para crear una instancia de `Cicla` con el tipo 'Montaña'
cicla = Cicla.crear_cicla_montana("Montaña")
# Llamamos al método `ciclaMONTANA` para mostrar la información sobre la cicla
cicla.ciclaMONTANA() # Salida esperada: La cicla es de tipo MONTANA para el deporte de MONTAÑA