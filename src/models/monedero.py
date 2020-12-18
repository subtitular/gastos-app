from pydantic import BaseModel

class monedero(BaseModel):
    id: int
    persona: persona
    tipo_monedero: tipo_monedero
    ultimo_balance: float