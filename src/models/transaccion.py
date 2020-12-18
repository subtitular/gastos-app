from pydantic import BaseModel

class transaccion(BaseModel):
    id: int
    origen: monedero
    destino: monedero
    fecha: datetime
    canal: canal
    valor: float