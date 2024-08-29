# se define la clase `Libro`
class Libro:
    
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        
    def prestar_libro(self):
        if self.disponible:
            self.disponible = False
            return True
        return False
    
    def devolver_libro(self):
        self.disponible = True
        
    def informacion_libro(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Título: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}\nEstado: {estado}"
        
class Miembro:
    def __init__(self, nombre, numero_membresia):
        self.nombre = nombre    
        self.numero_membresia = numero_membresia    
        self.libros_prestados = []
        
    def prestar_libros(self, libro):
        if libro.prestar_libro():
            self.libros_prestados.append(libro)
            return True 
        return False  
    
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver_libro()
            self.libros_prestados.remove(libro)
            return True
        return False
    
    def mostrar_libros_prestados(self):
        return [libro.titulo for libro in self.libros_prestados]
    
            
          
       
        
#crear instancias de la clase `Libro`
libro1 = Libro("1984", "George Orwell", "1234567890")
libro2 = Libro("To Kill a Mockingbird", "Harper Lee", "0987654321")
#se crea la instancia de `miembro`
miembro1 = Miembro("Angel Medina", "M001")


#Prestar libro
print("Intentando prestar '1984': ")
if miembro1.prestar_libros(libro1):
    print("Libro prestado con éxito.")
else:
    print("No se pudo prestar el libro.")
    
    
#Mostrar información del Libro
print("\nInformación del libro '1984': ")
print(libro1.informacion_libro())

# Mostrar libros prestados por el miembro
print("\nLibros prestados por Angel Medina:")
print(miembro1.mostrar_libros_prestados())

# Devolver un libro
print("\nIntentando devolver '1984':")
if miembro1.devolver_libro(libro1):
    print("Libro devuelto con éxito.")
else:
    print("No se pudo devolver el libro.")

# Mostrar información actualizada del libro
print("\nInformación del libro '1984' después de la devolución:")
print(libro1.informacion_libro())

# Mostrar libros prestados por el miembro después de la devolución
print("\nLibros prestados por Angel Medina después de la devolución:")
print(miembro1.mostrar_libros_prestados())