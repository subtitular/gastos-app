from pydantic import BaseModel

class tipo_frecuencia(BaseModel):
    id: int
    nombre: str
    unidad: unidad
    