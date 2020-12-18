from pydantic import BaseModel

class tipo_monedero(BaseModel):
    id: int
    nombre: str