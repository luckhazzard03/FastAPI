#parametro de rutas endpoints
from typing import List, Union
from fastapi import Path, Query, APIRouter
from fastapi.responses import JSONResponse
from src.models.movie_model import Movie, MovieCreate, MovieUpdate


movies: List[Movie] = []# lista de objetos tipo pelicula 


movie_router = APIRouter()

@movie_router.get ('/', tags=['Movies'], status_code=200, response_description='Nos debe devolver una respuesta exitosa')# codigo de respuesta para documentación
def get_movies() -> List[Movie]:# restornamos la listas de peliculas
    content = [movie.model_dump() for movie in movies]
    return JSONResponse( content = content, status_code=200)


#parametro de rutas
@movie_router.get ('/{id}', tags=['Movies'])
def get_movie(id: int = Path(gt=0)) -> Movie | dict: #se retorna una pelicula
    for movie in movies:
        if movie.id == id:
            return JSONResponse(movie.model_dump(), status_code=200)

    return JSONResponse(content={}, status_code=404)


#parametro de rutas
@movie_router.get('/movies/category', tags=['Movies'])
def get_movie_by_category(category: str = Query(min_length=3, max_length=20)) -> Union[List[Movie], dict]:
    # Aquí se asume que tienes una lista de películas y un método para filtrarlas por categoría
    filtered_movies = [movie for movie in movies if movie.category == category]
    if filtered_movies:
        return filtered_movies
    return {"message": "No movies found"}, 404# codigo de respuesta 2No encontrado"


# metodo crear Endpoints
@movie_router.post('/', tags=['Movies'])
def create_movie( movie: MovieCreate) ->List[Movie]:# Retornamos una lista de peliculas
    movies.append(movie)#REGISTRA EL OBJETO 
    content = [movie.model_dump() for movie in movies]
    return JSONResponse( content = content, status_code=201)# codigo de respuesta "creado"
    #return RedirectResponse('/movies', status_code=303) # redirige a la Url de inicio

# metodo actualizar Endpoints
@movie_router.put('/{id}', tags=['Movies'])
def update_movie(id: int, movie: MovieUpdate) ->List[Movie]: #retorna a una lista de peliculas 
    for item in movies:
        if item.id == id:                  # accedemos al atributo del objeto 
            item.title = movie.title       # accedemos al atributo del objeto 
            item.overview = movie.overview # accedemos al atributo del objeto 
            item.year = movie.year         # accedemos al atributo del objeto 
            item.rating = movie.rating     # accedemos al atributo del objeto 
            item.category = movie.category # accedemos al atributo del objeto 
    content = [movie.model_dump() for movie in movies]
    return JSONResponse( content = content, status_code=200) #codigo de respuesta ok
 


@movie_router.delete('/{id}', tags=['Movies']) 
def delete_movie(id: int) -> List[Movie]: #Retorna a una lista de peliculas
    for movie in movies:
        if movie.id == id:   
            movies.remove(movie)
    content = [movie.model_dump() for movie in movies]
    return JSONResponse( content = content, status_code=200)  #codigo de respuesta ok       

#Ruta para la vista de imagen 
#@ app.get('/get_file')
#def get_file():
#    return FileResponse('file.png')# retorna a la vista de la imagen