from service.auth.auth import get_password_hash
from config.db import conn
from model.user import users
from model.jugador import jugadores

def register_user():
    hashed_password = get_password_hash("password")
    user_insert = {"nombre": "admin", "email": "admin@admin.cl", "password": hashed_password, "disabled": False}
    if(not get_user_by_email(user_insert["email"])):
        conn.execute(users.insert().values(user_insert))
        conn.commit()

    return {"message": "User registered successfully"}

def get_user_by_email(email: str):
    return conn.execute(users.select().where(users.c.email == email)).first()

def get_jugador_by_email(email: str):
    return conn.execute(jugadores.select().where(jugadores.c.email == email)).first()

def get_jugador_by_id(id: int):
    return conn.execute(jugadores.select().where(jugadores.c.id == id)).first()