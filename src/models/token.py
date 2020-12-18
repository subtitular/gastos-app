from pydantic import BaseModel

class token(BaseModel):
    id: int
    tipo_token: tipo_token
    psk: str
    fecha_vigencia: datetime