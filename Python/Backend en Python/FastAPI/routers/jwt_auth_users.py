from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

# url: http://127.0.0.1:8000

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 2
SECRET = "156bf3d78b9e722a68d71d61b6068cecc6efec801c1adf83199d0c1673ebd7a5" #GENERATED WITH OPENSSL

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel): 
    username: str
    name_full: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

# data
users_db = {
    "ori28":{
        "username": "ori28",
        "name_full": "Oriana Colina",
        "email": "orianc28@gmail.com",
        "disabled": False,
        "password": "$2a$12$28fwRSBlyn7YkeN6POW7NOo/YKBtUtGW6XiX7vQAoX6k0b4GI6quK"
    },
    "carlos11":{
        "username": "carlos11",
        "name_full": "Carlos Martínez",
        "email": "carlosm11@gmail.com",
        "disabled": True,
        "password": "$2a$12$SyJFaCE0rDAX4Ui.EvCpk.zYjwA1TPodmiYeJI0z./5SlfmSoplEu"
    }
}

# return user without password
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

# return user with password incluided
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

# decode data from user
# if user exists its returned while this not is none
async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"})
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception

    return search_user(username)

# verify if user is disabled
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User not active")
    return user

# validates the form data sent in the POST
# if the data is correct, a token is returned, the duration of the token is 1 minute
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="The user is incorrect")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="The password is incorrect")
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)
    access_token = {"sub": user.username,
                    "exp": expire}
    return {
        "access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM),"token_type": "bearer"
    }

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
