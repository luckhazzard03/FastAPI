# # # Autor: Angel Medina
# # # Fecha: 02/09/2024
# #Herencia, Encapsulamiento, Abstracción, composición y interfaces


# Sistema de Notificaciones
# Enunciado:
# Crea un sistema de notificaciones que pueda enviar mensajes a través de diferentes canales
# (por ejemplo, correo electrónico, SMS y notificaciones push). Utiliza polimorfismo para 
# definir un método común enviar() en cada tipo de notificación.

# Pasos:
# Define una clase base abstracta Notificacion con un método abstracto enviar().
# Crea clases derivadas CorreoElectronico, SMS y NotificacionPush, cada una implementando el método enviar() de manera específica.
# Escribe una función enviar_notificacion() que tome un objeto de tipo Notificacion y llame al método enviar().
# En el bloque principal, crea instancias de CorreoElectronico, SMS y NotificacionPush, y usa enviar_notificacion()
# para enviar mensajes a través de cada canal.


from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self):
        pass
    
    
class CorreoElectronico(Notificacion):
    def __init__(self, direccion, mensaje):
        self.direccion = direccion
        self.mensaje = mensaje
        
    def enviar(self):
        return f"Enviando correo a la dirección: {self.direccion}, con el mensaje {self.mensaje}"
    
    
class SMS(Notificacion):
    def __init__(self, numero, mensaje):
        self.numero = numero
        self.mensaje = mensaje
        
    def enviar(self):
        return f"Enviando SMS al número{self.numero} con mensaje:{self.mensaje}"
    

class NotificacionPush(Notificacion):
    def __init__(self, dispositivo, mensaje):
        self.dispositivo = dispositivo
        self.mensaje = mensaje
    
    def enviar(self):
        return f"Enviando notificación Push al dispositivo {self.dispositivo}, con el mensaje {self.mensaje}"
    
    
def enviar_notificacion(notificacion: Notificacion):
    print(notificacion.enviar())
    

if __name__ == "__main__":
    
    notificaciones = [CorreoElectronico("luck@gmail.com", "Hola, ¿cómo estás?"),
                    SMS("+123456789", "Tu código de verificación es 1234"),
                    NotificacionPush("Dispositivo123", "Tienes una nueva actualización")]
    
    for notificacion in notificaciones:
        enviar_notificacion(notificacion)