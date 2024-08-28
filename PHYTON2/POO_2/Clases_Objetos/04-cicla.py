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


#Creamos el objeto
# Usamos el método de clase `crear_cicla_bmx` para crear una instancia de `Cicla` con el tipo 'BMXC'
cicla = Cicla.crear_cicla_bmx("BMXC")

# Llamamos al método `ciclaBMX` para mostrar la información sobre la cicla
cicla.ciclaBMX()  # Salida esperada: La cicla es de tipo BMXC para el deporte de BMX
