from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# url: http://127.0.0.1:8000

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel): 
    username: str
    name_full: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

usuarios_db = {
    "ori28":{
        "username": "ori28",
        "name_full": "Oriana Colina",
        "email": "orianc28@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "carlos11":{
        "username": "carlos11",
        "name_full": "Carlos Martínez",
        "email": "carlosm11@gmail.com",
        "disabled": True,
        "password": "1234"
    }
}

def buscar_usuario(username: str):
    if username in usuarios_db:
        return User(**usuarios_db[username])
    
def buscar_usuario_db(username: str):
    if username in usuarios_db:
        return UserDB(**usuarios_db[username])

async def current_user(token: str = Depends(oauth2)):
    usuario = buscar_usuario(token)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales de autenticación inválidas",
                            headers={"WWW-Authenticate": "Bearer"})
    if usuario.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Usuario no activo")
    return usuario

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    usuario_obtenido = usuarios_db.get(form.username)
    if not usuario_obtenido:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="El usuario es incorrecto")
    usuario = buscar_usuario_db(form.username)
    if not form.password == usuario.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="La contraseña es incorrecta")
    return {
        "access_token": usuario.username,
        "token_type": "bearer"
    }

@router.get("/users/me")
async def me(usuario: User = Depends(current_user)):
    return usuario
