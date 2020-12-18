from pydantic import BaseModel

class usuario(BaseModel):
    id: int
    alias: str
    tokens: []
    persona: persona
    fecha_ingreso: datetime
