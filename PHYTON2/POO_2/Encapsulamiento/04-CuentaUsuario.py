# Autor: Angel Medina
# Fecha: 30/08/2024
# Clases, objetos Encapsulamiento 

# Diseña una clase llamada CuentaUsuario para gestionar la información de una cuenta de usuario en una aplicación. La clase debe incluir:

# Atributos:

# __usuario (privado): El nombre de usuario.
# __contrasena (privado): La contraseña del usuario.
# Métodos:

# __init__(self, usuario, contrasena): Constructor que inicializa los atributos.
# cambiar_contrasena(self, contrasena): Método para cambiar la contraseña del usuario. La nueva contraseña debe tener al menos 8 caracteres.
# verificar_usuario(self, usuario): Método para verificar si el nombre de usuario coincide con el proporcionado.
# __str__(self): Método que devuelve una cadena con el nombre de usuario (la contraseña debe permanecer oculta).
# Objetivo: Asegúrate de que la contraseña esté protegida y que el acceso a los datos sensibles esté restringido mediante métodos controlados.

#Definimos la clase `CuentaUsuario`
class CuentaUsuario:
    # Constructor de la clase
    def __init__(self, usuario, password):
         # Inicializa los atributos privados __usuario y __password
        self.__usuario = usuario
        self.__password = password
    #Método para cambiar la contraseña
    def cambiar_password(self, password):
        if len(password) >=8:
            self.__password =password
        else:
            print("La contraseña debe tener al menos 8 caracteres.")
    #Método para verificar usuario        
    def verificar_usuario(self, usuario):
         # Retorna una cadena de texto formateada con los valores actuales de los atributos
        return self.__usuario == usuario 
    
    # Método especial para obtener una representación en cadena del objeto
    def __str__(self):
        return(f"Ususario: {self.__usuario} Contraseña: {self.__password}")
 
 
#Creación de la instancia de la clase `CuentaUsuario`
cuenta = CuentaUsuario("Lucky05", "securepass123")
print(cuenta.verificar_usuario("Lucky05"))  # Salida: True
cuenta.cambiar_password("newpassword")
print(cuenta)  # Salida: Usuario: Lucky05
  
              