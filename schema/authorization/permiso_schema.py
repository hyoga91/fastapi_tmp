from pydantic import BaseModel, ConfigDict

class Permiso(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    id: str
    nombre: str
