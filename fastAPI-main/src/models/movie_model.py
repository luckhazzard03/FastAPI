
#consulta de datos y registrar 
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, field_validator


class Movie(BaseModel):
    #de tipo opcional el Id
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str


#consulta de DATOS  y ACTUALIZA  
class MovieUpdate(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str


#consulta de DATOS y REGISTRA
class MovieCreate(BaseModel):
    #de tipo opcional el Id
    id: int
    title: str 
    overview: str  
    year: int 
    rating: float 
    category: str

    # validación para minimo y maximo en caracteres "TITLE"
    @field_validator('title')
    def validate_title(cls, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError('Title length must be between 5 and 15 characters')
        return value

    # validación para minimop y maximo en caracteres "OVERVIEW"
    @field_validator('overview')
    def validate_overview(cls, value):
        if len(value) < 5 or len(value) > 50:
            raise ValueError('Overview length must be between 5 and 50 characters')
        return value
    
    # validación para la fecha que sea <= al año 1900 y >= a 2024 "YEAR"
    @field_validator('year')
    def validate_year(cls, value):
        current_year = datetime.now().year
        if value < 1900 or value > current_year:
            raise ValueError(f'Year must be between 1900 and {current_year}')
        return value
    
     # validación para minimo y maximo en caracteres "RATING"
    @field_validator('rating')
    def validate_rating(cls, value):
        if value < 0 or value > 10:
            raise ValueError('Rating must be between 0 and 10')
        return value
    
     # validación para minimo y maximo en caracteres "CATEGORY"
    @field_validator('category')
    def validate_category(cls, value):
        if len(value) < 5 or len(value) > 20:
            raise ValueError('Category length must be between 5 and 20 characters')
        return value
    

class config:
    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                'title':'My movie',
                'overview':'Esta pelicula trata acerca ...',
                'year':2022,
                'rating':5,
                'category':'comedia',
            }
        }
    }

   


movies: list[Movie] = []