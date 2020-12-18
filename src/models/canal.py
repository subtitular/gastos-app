from pydantic import BaseModel

class canal(BaseModel):
    id: int
    tipo_canal: tipo_canal
    nombre: str
    