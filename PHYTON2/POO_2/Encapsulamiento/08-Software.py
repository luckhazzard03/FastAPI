# # # Autor: Angel Medina
# # # Fecha: 05/09/2024
# # # Clases, objetos Encapsulamiento Polimorfismo y instacia de objetos


#  Sistema de Gestión de Proyectos de Software
# Enunciado:
# Diseña un sistema para gestionar proyectos de software. Incluye una clase base Proyecto y 
# clases derivadas como ProyectoAgil y ProyectoTradicional. Implementa métodos para planificación, 
# seguimiento y entrega.

# Requisitos:
# Proyecto debe tener atributos privados para nombre, presupuesto y fecha de inicio.
# ProyectoAgil debe incluir un atributo privado para número de sprints.
# ProyectoTradicional debe tener un atributo privado para fases del proyecto.
# Implementa un método protegido en Proyecto para calcular la duración estimada.
# Sobrescribe el método de seguimiento en las clases derivadas para reflejar diferentes metodologías.
# Explicación:
# Encapsulamiento: Uso de atributos privados y métodos protegidos.
# Herencia: ProyectoAgil y ProyectoTradicional heredan de Proyecto.
# Polimorfismo: Sobrescritura del método de seguimiento.

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

##Definimos la clase `Proyecto`
class Proyecto(ABC):
    def __init__(self, nombre, presupuesto, fecha_inicio):
        self.__nombre = nombre
        self.__presupuesto = presupuesto
        self.__fecha_inicio =  datetime.strptime(fecha_inicio, "%Y-%m-%d")
    
    @property  
    def nombre(self):
        """
    Propiedad que devuelve el nombre del proyecto.

    Esta propiedad permite acceder al atributo privado __nombre
    de forma controlada, proporcionando acceso de solo lectura.

    Returns:
        str: El nombre del proyecto.
    """
        return self.__nombre
    
    @property
    def presupuesto(self):
        return self.__presupuesto
    
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    
      
    def _calcular_duracion_estimada(self):
        #Método protegido para calcular la duración estimada 
        #Asumidos 1 mes por cada 10,000 de presupuesto
        meses = self.__presupuesto // 10000
        return self.__fecha_inicio + timedelta(days=30 * meses)
    
    def planificacion(self):
        return f"Planificación del proyecto {self.__nombre} iniciada."
    
    @abstractmethod
    def seguimiento(self):
        pass
    
    def entrega(self):
        return f"Proyecto {self.__nombre} entregado."
    
class ProyectoAgil(Proyecto):
    def __init__(self, nombre, presupuesto, fecha_inicio, num_sprints):
        super().__init__(nombre, presupuesto, fecha_inicio)
        self.__num_sprints = num_sprints
        
    def seguimiento(self):
        return f"Seguimiento Ágil del proyecto { self.nombre}. Sprint actual: { self.__num_sprints // 2}"
    
    def planificar_sprint(self):
        return f"Planificación del Sprint para {self.nombre}. Total de sprints: {self.__num_sprints}"
    
class ProyectoTradicional(Proyecto):
    def __init__(self, nombre, presupuesto, fecha_inicio, fases):
        super().__init__(nombre, presupuesto, fecha_inicio)
        self.__fases = fases
        
    def seguimiento(self):
        return f"Seguimiento Ágil del proyecto { self.nombre}. Fase actual: { self.__fases[len(self.__fases) // 2]}"
    
    def revisar_fase(self):
        return f"Revisión de la fase para  para {self.nombre}. Fases del proyecto: {', '.join(self.__fases)}"
    
def gestionar_proyecto(proyecto):
    print(proyecto.planificacion())
    print(f"Fecha de inicio: {proyecto.fecha_inicio.strftime('%Y-%m-%d')}")
    print(f"Fecha estimada de finalización: {proyecto._calcular_duracion_estimada().strftime('%Y-%m-%d')}")
    print(proyecto.seguimiento())
    if isinstance(proyecto, ProyectoAgil):
        print(proyecto.planificar_sprint())
    elif isinstance(proyecto, ProyectoTradicional):
        print(proyecto.revisar_fase())
    print(proyecto.entrega())
    print()
        
        
#creación de instancias
proyecto_agil = ProyectoAgil("Sistema de Ventas Online", 50000, "2024-01-01",10)
proyecto_tradicional = ProyectoTradicional("Sistema Bancario", 100000, "2024-02-01",["Análisis", "Diseño", "Implementación", "Pruebas", "Despliegue"])

#Demostración de uso
proyectos = [proyecto_agil, proyecto_tradicional]
for proyecto in proyectos:
    gestionar_proyecto(proyecto)
        
            
        
        