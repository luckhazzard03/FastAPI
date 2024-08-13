animal = " shit Zut "
print(animal.upper())#todas en mayusculas
print(animal.lower())# pone todas en minuscula
print(animal.strip().capitalize())# la primera letra la pasa a mayuscula
print(animal.title())# la primeras letras la pasa a mayuscula
print(animal.strip())# borra los espacios del inicio y final
print(animal.find("hi"))# devuelve el indice del caracter 
print(animal.replace("hit", "j"))# remplaza por el  "hit" por el caracter "j" 
print(animal.replace("hit", "j").find("u"))# remplaza por el  "hit" por el caracter "j" 
print("it" in animal)# esta funcionalidad me devuelve un boolean True
print("it"  not in animal)# esta funcionalidad me devuelve un boolean que no se encuentra False