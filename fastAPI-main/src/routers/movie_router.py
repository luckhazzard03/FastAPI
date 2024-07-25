from typing import List
from fastapi import Path, Query, APIRouter
from fastapi.responses import JSONResponse
from src.models.movie_model import Movie, MovieCreate, MovieUpdate

movies: list[Movie] = []
movie_router = APIRouter()# CONTIENE LAS RUTAS QUE TENGAN QUE VER CON PELICULAS


# end point segunda ruta
@movie_router.get('/', tags=['Movies'], status_code=200, response_description='Nos debe devolver una respuesta exitosa ')#, status_code=200 para cuestion de documentación 
# se crea la funcion para ejecutar la ruta 
def get_movies() -> List[Movie]:
    content = [movie.model_dump() for movie in movies]
    #retorna el mensaje "movies"
    return JSONResponse(content=content, status_code=200)


# end point Tercera ruta 
@movie_router.get('/{id}', tags=['Movies'])
# se crea la funcion para ejecutar la ruta 
def get_movie(id: int = Path(gt=0)) -> Movie | dict:
    # itera cada movie en cada movies
    for movie in movies:
        if movie.id == id:
            #se convierte en diccionarios
            return JSONResponse(content=movie.model_dump(),status_code=200) 
    return  JSONResponse(content={}, status_code=404)  



# End point para obtener películas filtradas por categoría
@movie_router.get('/by_category', tags=['Movies'])
def get_movie_by_category(category: str = Query(min_length=5, max_length=20)) -> Movie | dict:
    filtered_movies = [movie.model_dump() for movie in movies if movie.category == category]
    if filtered_movies:
        return JSONResponse(content=filtered_movies, status_code=200)
    else:
        return JSONResponse(content={}, status_code=404)


#METODO POST
# end point para crear una nueva película
@movie_router.post('/', tags=['Movies'])
def create_movie(movie: MovieCreate) -> List[Movie]:
    new_movie = Movie(**movie.model_dump())
    movies.append(new_movie)
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=201)
#METODO PUT
# end point primer ruta PARA PUT
@movie_router.put('/{id}', tags=['Movies'])
#Función para EDITAR
def update_movie(id: int, movie:MovieUpdate)-> List[Movie]:
    
    for item in movies:
        if item.id == id:
             item.title = movie.title
             item.overview = movie.overview
             item.year = movie.year
             item.rating = movie.rating
             item.category = movie.category
    content = [movie.model_dump() for movie in movies]
    #retorna el mensaje "movies"
    return JSONResponse(content=content, status_code=200)

#METODO DELETE
# end point primer ruta PARA DELETE
@movie_router.delete('/{id}', tags=['Movies'])
def delete_movie(id: int)-> List[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
    content = [movie.model_dump() for movie in movies]
    #retorna el mensaje "movies"
    return JSONResponse(content=content, status_code=200)


#METODO GET "FileResponse" respuesta tipo archivos para enviar 
#@app.get('/get_file')
#def get_file():
    #return FileResponse('file.pdf.txt')
