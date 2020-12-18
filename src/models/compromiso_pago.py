from pydantic import BaseModel

class compromiso_pago(BaseModel):
    id: int
    tipo_pago: tipo_pago
    remitente: persona
    destinatario: persona
    periodo: periodo
    valor: float