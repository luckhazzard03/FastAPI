# Autor: Angel Medina
# Fecha: 19/08/2024
# Clases, objetos y Herencia 

#Sistema de empleados Construye una jerarquía de clases para representar
# diferentes tipos de empleados en una empresa. Crea una clase base llamada Empleado y
# dos clases derivadas: EmpleadoTiempoCompleto y EmpleadoMedioTiempo.


# Se define la clase Padre `Empleado`
class Empleado:
    #Método constructor para inicializar los atributos 
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base
        
    #Método  calcular sueldo 
    def calcular_sueldo(self):
        return self.sueldo_base
    
    #Método para obtener una representación en cadena del Objeto 
    def __str__(self):
        return (f"Nombre del empleado {self.nombre} su sueldo base: {self.calcular_sueldo()}")
 
 
 #Definimos la clase ` EmpleadoTiempoCompleto`    
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, sueldo_base, bonificacion):
        #llamada del método constructor de la clase `Empleado`
        super().__init__(nombre, sueldo_base)
        #Atributo específico de la clase `EmpleadoTiempoCompleto`
        self.bonificacion = bonificacion
        
    #Método sobreescrito para calcula4r el sueldo ()
    def calcular_sueldo(self):
        return self.sueldo_base + self.bonificacion
    
    
#Definimos la clase `EmpleadoMedioTiempo`
class EmpleadoMedioTiempo(Empleado):    
    def __init__(self, nombre, sueldo_base, horas_trabajadas):
        #llamado del método constructor de la clase Padre `Empleado`
        super().__init__(nombre, sueldo_base)
        #Atributo específico de la clase `EmpleadoMedio Tiempo`
        self.horas_trabajadas = horas_trabajadas
        
    #Método para calcular el sueldo de medio tiempo 
    def calcular_sueldo(self):
        return self.sueldo_base * (self.horas_trabajadas / 40) # Sueldo base * hora, asumiendo 40 horas a la semana         
    
    
     
# Se crea las instancias de las clases `EmpleadoTiempoCompleto`  y `EmpleadoMedioTiempo` 
empleadoTiempoCompleto = EmpleadoTiempoCompleto("Angel",900000, 45000)      
empleadoTiempoMedio = EmpleadoMedioTiempo("Adrian",450000, 20)   #Sueldo base por hora 

print(empleadoTiempoCompleto)   
print(empleadoTiempoMedio)   