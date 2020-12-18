from pydantic import BaseModel

class tipo_pago(BaseModel):
    id: int
    nombre: str
    descripcion: str
    frecuencia: frecuencia
    