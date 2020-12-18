from pydantic import BaseModel

class frecuencia(BaseModel):
    id: int
    nombre: str
    tipo_frecuencia: tipo_frecuencia
    periodos: []
    