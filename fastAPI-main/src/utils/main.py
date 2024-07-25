from fastapi import FastAPI, Depends, Query
from fastapi.requests import  Request
from fastapi.responses import  PlainTextResponse, Response, JSONResponse
from src.routers.movie_router import movie_router
from src.utils.http_error_handler import HTTPErrorHandler
from typing import Annotated

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os







# crea una instancia de fastapi "app"
app = FastAPI()
app.title = "App fastAPI"

#DEFINIMOS EL middleware
app.add_middleware(HTTPErrorHandler)

static_path = os.path.join(os.path.dirname(__file__), 'static/')
templates_path = os.path.join(os.path.dirname(__file__), 'templates/')


app.mount('/static', StaticFiles(directory=static_path), 'static')
templates= Jinja2Templates(directory=templates_path)

@app.middleware('http')
async def http_error_handler(request: Request, call_next)->Response | JSONResponse:
    print('Middleware is runnig!')
    return await call_next(request)# verificar en el router 


#METODO GET
# end point primera ruta 
@app.get('/', tags=['Home'])
# se crea la funcion para ejecutar la ruta 
def home(request:Request):
    #retorna el mensaje "Home"
    return templates. TemplateResponse('index.html', { 'request': request,'message': 'Welcome' })


#def common_params(start_date:str, end_date: str):
#    return { "start_date": start_date, "end_date":end_date}

#CommonDep = Annotated[dict, Depends(common_params)]

class CommonDep:

    def __init__(self, start_date:str, end_date: str)-> None:
        self.star_date =  

#RUTA para los usuarios
@app.get('/users')
def get_users( commons:CommonDep ):
    return f"Users created between {commons['start_date']} and {commons['end_date']}"


#RUTA para Clientes
@app.get('/customers')
def get_customers(commons: CommonDep):
    return f"Customers created between  {commons['start_date']} and {commons['end_date']}"



app.include_router(prefix='/movies', router=movie_router)


