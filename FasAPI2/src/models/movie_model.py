import datetime
from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str
    
class MovieCreate(BaseModel):
    id: int
    title: str 
    overview: str = Field(min_length=15, max_length=50)#Validacion de caracteres minimo maximo
    year: int = Field(le=datetime.date.today().year, ge=1900)#validación de fecha minimo de año 1900
    rating: float = Field(ge=0, le =10)# minimo maximo
    category: str = Field(min_length=3, max_length=20)# #Validación de caracteres 
    
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                'title':'My movie',
                'overview':'Esta pelicula trata de ...',
                'year':'2024',
                'rating':10,
                'category':'Acción'
            }
        }
    }
 
 
 
    
class MovieUpdate(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str