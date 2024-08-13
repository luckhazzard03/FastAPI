class Persona:
    contador_personas = 0 #Variable definida 
    #definimos el constructor de la clase con el metodo inicializador
    def __init__(self, nombre, apellido):
        self.nombre = nombre #definimos el atributo de Nombre
        self.apellido = apellido #definimos el atributo de apellido

# Mostrar los atributos de un objeto
persona1 = Persona('Juan','Perez') # Creamos un Objeto
print(persona1.__dict__) #saber cuales son los atributos de instancia del objeto

# Crear un atributo en el momento
print(persona1.contador_personas) # Accediendo al atributo de clase
# Pero no es posible modificarlo con el objeto, sino con la clase
persona1.contador_personas = 10
print(persona1.__dict__)
# El atributo anterior oculta al atributo de clase
print(Persona.contador_personas) # Atributo clase
print(persona1.contador_personas) # Atributo del objeto 1

# Un segundo objeto
persona2 = Persona('Karla', 'Gomez')
print(persona2.__dict__)
print(persona2.contador_personas)

# Asociar un atributo de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2)

# Desde los objetos creados, accedemos al nuevo atributo de la clase
# Esto es posible por que los atributos de clase se comparten con todos los objetos
print(persona1.contador2)
print(persona2.contador2)