from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from jose import jwt
from decouple import config
import bcrypt

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# Obtiene la clave secreta desde las variables de entorno
JWT_SECRET_KEY = config('JWT_SECRET_KEY')

# Usuarios con contraseñas hasheadas
users = {
    "Angel": {"username": "Angel", "email": "eduar19311@hotmail.com", "password_hash": bcrypt.hashpw("BuckAslam27".encode(), bcrypt.gensalt())},
    "Emmanuel": {"username": "Emmanuel", "email": "Emmanuel19311@hotmail.com", "password_hash": bcrypt.hashpw("BuckAslam28".encode(), bcrypt.gensalt())},
}

# Función para codificar un token JWT
def encode_token(payload: dict) -> str:
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
    return token

# Función para decodificar un token JWT
def decode_token(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        data = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        user = users.get(data["username"])
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Ruta para generar token JWT (autenticación)
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users.get(form_data.username)
    if not user or not bcrypt.checkpw(form_data.password.encode(), user["password_hash"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = encode_token({"username": user["username"], "email": user["email"]})
    return {"access_token": token, "token_type": "bearer"}

# Ruta protegida que requiere token JWT (autorización)
@app.get("/users/profile")
def profile(my_user: dict = Depends(decode_token)):
    return my_user
