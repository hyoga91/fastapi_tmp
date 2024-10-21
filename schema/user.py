from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    id: str | None = None
    nombre: str
    email: str
    password: str
    disabled: bool = None

class UserLogin(BaseModel):
    email: str
    password: str