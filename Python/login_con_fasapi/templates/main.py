from fastapi import FastAPI, Request, Form, HTTPException, Cookie
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Annotated
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from db import get_users
import bcrypt

SECRET_KEY = "9f68ec2e0cef2bd0907430ff0aea2c78ad96bcc67e6fbe3d615dc890ed131921"
TOKEN_SECONDS_EXPIRE = 25

users = get_users()

def create_token(username: str):
    data_token = {"username": username}
    data_token["exp"] = datetime.now(timezone.utc) + timedelta(seconds=TOKEN_SECONDS_EXPIRE)
    token_jwt = jwt.encode(data_token, key=SECRET_KEY, algorithm="HS256")
    return token_jwt

def get_user(username: str, users: dict):
    return users.get(username)

def authenticate_user(stored_password: str, provided_password: str):
    return bcrypt.checkpw(provided_password.encode("utf-8"), stored_password.encode("utf-8"))

app = FastAPI()

jinja2_templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return jinja2_templates.TemplateResponse("index.html", {"request": request})

@app.get("/users/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, access_token: Annotated[str | None, Cookie()] = None):
    if access_token is None:
        return RedirectResponse("/", status_code=302)
    try:
        data_user = jwt.decode(access_token, key=SECRET_KEY, algorithms=["HS256"])
        username = data_user.get("username")
        if get_user(username, users) is None:
            return RedirectResponse("/", status_code=302)
        return jinja2_templates.TemplateResponse("dashboard.html", {"request": request})
    except JWTError:
        return RedirectResponse("/", status_code=302)

@app.post("/users/login")
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    user_data = get_user(username, users)
    if not user_data:
        raise HTTPException(status_code=401, detail="No autorizado")
    
    if not authenticate_user(user_data["password"], password):
        raise HTTPException(status_code=401, detail="No autorizado")
    
    token = create_token(username)
    
    return RedirectResponse(
        "/users/dashboard",
        status_code=302,
        headers={
            "set-cookie": f"access_token={token}; Max-Age={TOKEN_SECONDS_EXPIRE}; HttpOnly"
        }
    )

@app.post("/users/logout")
def logout():
    return RedirectResponse("/", status_code=302, headers={
        "set-cookie": "access_token=; Max-Age=0; HttpOnly"
    })
