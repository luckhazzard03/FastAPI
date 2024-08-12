from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


#Creación de la aplicación 
app = FastAPI()



class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    
 #Implementación del Manejador de Base de Datos   
class DBManager:
    def __init__(self) -> None:
        self.db = {}
        
    def get(self, id: int):
        return self.db.get(id)
    
    def insert(self, id: int, item: Item):
        self.db[id] = item
    
    def delete(self, id: int):
        if id in self.db:
            del self.db[id]
        else:
            raise HTTPException(status_code=404, detail="Item not found")
        
# SE CREA lA instancia  DBManager, que se usa para manejar los items en la base de datos    
db_manager = DBManager()

# ruta get leer un item 
@app.get("/item/{item_id}")
def read_item(item_id: int, q: Union[str, None]= None):
    item = db_manager.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": item, "query": q}


#Actualizar un Item
@app.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    db_manager.insert(item_id, item)
    return {"item_name": item.name, "item_id": item_id}


#eliminar Ítem 
@app.delete("/item/{item_id}")
def delete_item(item_id: int):
    db_manager.delete(item_id)
    return {"detail": "Item deleted successfully"}


"""
uvicorn test:app --reload
"""