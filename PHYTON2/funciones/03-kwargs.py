def get_product(**datos):# los kwargs "**" en este caso serian parametros
    print(datos["id"], datos["name"])# imprimimos nuestros parametros 
    

# nos imprime {'id': 'id'} el nombre del parametro esto es un diccionario    
get_product(id="23",
            name="iPhone",
            desc="Esto es un iPhone")