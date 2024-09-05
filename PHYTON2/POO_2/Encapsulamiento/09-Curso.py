#  Autor: Angel Medina
# Fecha: 05/09/2024
# Clases, objetos Encapsulamiento Polimorfismo y instacia de objetos

# Sistema de Gestión de Cursos en Línea
# Enunciado:
# Diseña un sistema para gestionar cursos en una plataforma educativa en línea. Incluye una clase base Curso y
# clases derivadas como CursoEnVivo y CursoAutodirigido. Implementa métodos para inscripción,
# seguimiento del progreso y evaluación.

# Requisitos:
# Curso debe tener atributos privados para título, duración (en semanas) y precio.
# CursoEnVivo debe incluir un atributo privado para horario de sesiones en vivo.
# CursoAutodirigido debe tener un atributo privado para número de módulos.
# Implementa un método protegido en Curso para calcular la fecha de finalización estimada.
# Sobrescribe el método de seguimiento de progreso en las clases derivadas para reflejar diferentes metodologías.

# Explicación:
# Encapsulamiento: Uso de atributos privados y métodos protegidos.
# Herencia: CursoEnVivo y CursoAutodirigido heredan de Curso.
# Polimorfismo: Sobrescritura del método de seguimiento de progreso.


from datetime import datetime, timedelta

#Definimos la clase  `Curso`
class Curso:
    def __init__(self, titulo, duracion_semanas, precio):
        
        self.__titulo = titulo
        self.__duracion_semanas = duracion_semanas
        self.__precio = precio
        self.__inscritos = []
        
        
    def inscribir(self, estudiante):
        self.__inscritos.append(estudiante)
        print(f"{estudiante} inscrito en {self.__titulo}")
        
    def __calcular_fecha_finalizacion(self):
        fecha_inicio = datetime.now()
        return fecha_inicio + timedelta(weeks=self.__duracion_semanas)
    
    def seguimiento_progreso(self):
        pass
    
    def evaluar(self, estudiante):
        print(f"Evaluación de  {estudiante} en {self.__titulo}:")
        #Lógica de evaluación básica; puede ser sobreescrita por clases derivadas
        print("Evaluación completada con éxito.")
        
        
#Definimos la clase derivada `CursoEnVivo`
class CursoEnVivo(Curso):
    def __init__(self, titulo, duracion_semanas, precio, horario_sesion):
        super().__init__(titulo, duracion_semanas, precio)
        self.__horario_sesion = horario_sesion
        
    def seguimiento_progreso(self):
        return f"Progreso del curso en vivo {self.__titulo}:"
    
#Definimos la clase derivada `CursoAutodirigido`
class CursoAutodirigido(Curso):
    def __init__(self, titulo, duracion_semanas, precio, num_modulos):
        super().__init__(titulo, duracion_semanas, precio)
        self.__num_modulos = num_modulos
        
    def seguimiento_progreso(self):
        return f"Progreso del curso autodirigido {self.__titulo}: "
    
    
    
# se instancia las clases derivadas
curso_en_vivo = CursoEnVivo("Introducción a Python ", 8, 120, "Lunes y miercoles 19:00-21:00")
curso_autodirigido = CursoAutodirigido("Data Science para principiantes", 10, 150, 12)


curso_en_vivo.inscribir("Angel Medina")
curso_autodirigido.inscribir("Adriana Bello")


curso_en_vivo.seguimiento_progreso()
curso_autodirigido.seguimiento_progreso()

curso_en_vivo.evaluar("angel Medina")
curso_autodirigido.evaluar("Adriana Bello")

