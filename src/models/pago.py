from pydantic import BaseModel

class pago(BaseModel):
    id: int
    compromiso_pago: compromiso_pago
    observacion: str
    transaccion: []
