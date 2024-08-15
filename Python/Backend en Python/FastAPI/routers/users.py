from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["users"]) #instancing from FastAPI

#create user
class User(BaseModel): #BaseModel it's a parameter and constructor not necessary
    id: int
    nombre: str
    apellido: str
    edad: int

#creating array users object
users_array = [User(id = 1, nombre="Oriana", apellido="Colina", edad=34),
         User(id = 2, nombre="Ronald", apellido="Pérez", edad=24),
         User(id = 3, nombre="Miguel", apellido="Díaz", edad=15)]

#get all users
@router.get("/users")
async def users():
    return users_array

#get user by id
@router.get("/user/{id}")
async def user(id:int):
    return search(id)

#use a query for get user by id
@router.get("/userquery/") #example: /usersquery/?id=1&nombre="Oriana" return user one.
async def user(id:int):
    return search(id)

@router.post("/user/", response_model=User, status_code=201)
async def add_user(user: User):
    if type(search(user.id))==User:
        raise HTTPException(status_code=204, detail="El usuario ya se encuentra registrado") 
    users_array.append(user)
    return user

@router.put("/user/")
async def update_user(user: User):
    found = False
    for index, user_saved in enumerate(users_array):
        if user_saved.id == user.id:
            users_array[index] = user
            found = True
    if not found:
         return {"error":"No se ha actualizado el usuario"}
    return user

@router.delete("/user/{id}")
async def delete_user(id:int):
    found = False
    for index, user_saved in enumerate(users_array):
        if user_saved.id == id:
            del users_array[index]
            found = True
    if not found:
         return {"error":"No se ha eliminado el usuario"}
    return users_array
    
#fuction search user by id 
def search(id):
    users = filter(lambda user:user.id == id, users_array)
    try:
        return list(users)[0] #return user
    except:
        return {"error":"No se encontró el usuario"} #if user no found return error

