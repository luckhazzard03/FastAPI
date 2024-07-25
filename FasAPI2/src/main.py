from fastapi import FastAPI, Request, Depends
from src.routers.movie_router import movie_router
from src.utils.http_error_handler import HTTPErrorHandler
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os


app = FastAPI()

app.title = "FastAPI2"
app.version = "2.0.0"


app.add_middleware(HTTPErrorHandler)

static_path = os.path.join(os.path.dirname(__file__), 'static/')# se unen dos directorios 
templates_path = os.path.join(os.path.dirname(__file__), 'templates/')# carpeta para los templates 

app.mount('/static', StaticFiles(directory= static_path), 'static')
templates = Jinja2Templates(directory=templates_path)



@app.get ('/', tags=['Home'])
def home(request: Request):
    return templates.TemplateResponse('index.html', { 'request':request,'message': 'Welcome'})

#DEPENDENCIAS
def common_params(start_date: str, end_date: str):
    return { "start_date": start_date, "end_date": end_date}

CommonDep= Annotated[dict, Depends(common_params)]

@app.get('/users')
def get_users(commons: CommonDep):
    return f"Users created between {commons['start_date']} and {commons['end_date']}"



@app.get('/custumers')
def get_custumers(commons: CommonDep):
    return f"Custumers created between {commons['start_date']} and {commons['end_date']}"

app.include_router(prefix='/movies', router=movie_router)

