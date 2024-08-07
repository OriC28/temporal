from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError
from models.user import Users
from config.db import session
from cryptography.fernet import Fernet
from pydantic import BaseModel, EmailStr, Field

key = Fernet.generate_key()
f = Fernet(key)
user = APIRouter()

# Model (contains validations)
class User(BaseModel):
    name: str = Field(min_length=3, max_length=25)
    email: EmailStr
    password: str = Field(min_length=8, max_length=50)

# get all users
@user.get("/", tags=['Users'])
def get_users():
    query = session.query(Users).all()
    return query

# insert a new user
@user.post("/", tags=['Users'])
async def create_user(user: User):
    try:
        user_instance = Users(name=user.name, email=user.email, password=f.encrypt(user.password.encode("utf-8")))
        session.add(user_instance)
        session.commit()
        return {"status": "success", "message": "El usuario se ha agregado"}, status.HTTP_201_CREATED
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El usuario no se ha agregado: email ya existe")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"El usuario no se ha agregado: {str(e)}")
    
# get an user by id
@user.get("/{id}", tags=['Users'])
async def get_user(id: str):
    query = (session.query(Users).filter(Users.id == id)).first()
    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail="No se ha encontrado")
    return query

#update an user by id
@user.put("/{id}", tags=['Users'])
async def update_user(id: str, new_name: str = None, new_email: str = None, new_password: str = None):
    user_instance = session.query(Users).filter(Users.id == id).first()
    
    if not user_instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    
    if not new_name and not new_email and not new_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Se requiere al menos un campo para actualizar")

    if new_name:
        user_instance.name = new_name
    if new_email:
        user_instance.email = new_email
    if new_password:
        user_instance.password = f.encrypt(new_password.encode("utf-8"))
    
    try:
        session.commit()
        return {"status": "success", "message": "Usuario modificado con éxito"}
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El email ya existe")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al actualizar el usuario: {str(e)}")

# delete an user by id
@user.delete("/{id}", tags=['Users'])
async def delete_user(id: str):
    query = (session.query(Users).filter(Users.id == id)).first()
    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail="No se ha encontrado el usuario a eliminar")
    session.delete(query)
    session.commit()
    raise HTTPException(status_code=status.HTTP_200_OK,  detail="El usuario se ha eliminado con éxito")



