from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from jose import jwt
from decouple import config  # Importa config de decouple


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "/token ")


# Obtiene la clave secreta desde las variables de entorno
JWT_SECRET_KEY = config('JWT_SECRET_KEY')


users = {
    "Angel": {"username": "Angel", "email": "eduar19311@hotmail.com", "password": "BuckAslam27"},
    "Emmanuel": {"username": "Emmanuel", "email": "Emmanuel19311@hotmail.com", "password": "BuckAslam28"},
}


#Función para Codificar un Token JWT:
def encode_token(payload: dict) -> str:
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")# se debe guardar en una variable de entorno o en un lugar que no sea visible
    return token


#Función para Decodificar un Token JWT:
def decode_token(token: str = Depends(oauth2_scheme)) -> dict:
    data = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
    user = users.get(data["username"])
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user


#Ruta para Generar Token JWT (Autenticación):
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users.get(form_data.username)
    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=400, detail="Incorrect username or password")# se valida que la contraseña pertenesca al usuario
    token = encode_token({"username": user["username"], "email": user["email"]})
    return {"access_token": token, "token_type": "bearer"}

    
#Ruta Protegida que Requiere Token JWT (Autorización):    
@app.get("/users/profile")
def profile(my_user: dict = Depends(decode_token)):
    return my_user
