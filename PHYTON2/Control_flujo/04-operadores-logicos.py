# and, or, not 
#"""
# AND = Devuelve True si ambos elementos son True 	"True and True = True"
# OR = Devuelve True si al menos un elemento es True  "True or False = True"
# pero si ambos son False  el resultado es False      
# 
# NOT = Devuelve el contrario, True si es Falso y viceversa "not True = False""" 

gas = False
encendido = True
edad = 18

# se ejecuta de DERECHA a IZQUIERDA POR LOS PARENTESIS 
#IMPRIME VERDADERO
if not gas and (encendido or edad > 17):
    print("Puedes avanzar")

#Operaciones de corto circuito se ejecuta de izquierda a derecha
if not gas and encendido and edad > 17:
    print("Puedes avanzar al siguiente")
