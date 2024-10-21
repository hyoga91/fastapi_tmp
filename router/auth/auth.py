from fastapi import Depends, APIRouter, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from config.db import conn
from model.user import users
from schema.auth.token import Token
from schema.user import User
from service.jugador import create_jugador
from utils.create_admin import get_user_by_email
from service.auth.auth import ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_user, create_access_token, get_current_user, get_password_hash

auth = APIRouter()

@auth.post("/register/")
def register_user(user: User):
    if get_user_by_email(user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    print(user)
    hashed_password = get_password_hash(user.password)
    user_insert = {"nombre": user.nombre, "email": user.email, "password": hashed_password, "disabled": False}
    create_jugador(user)
    conn.execute(users.insert().values(user_insert))
    conn.commit()

    return {"message": "User registered successfully"}

@auth.post("/token", response_model=Token)
async def login_for_access_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends() 
) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    response.set_cookie(key="access_token", value=access_token, httponly=True)

    return Token(access_token=access_token, token_type="bearer")

@auth.get("/protected-route")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello,{current_user.nombre} you're authenticated!"}



