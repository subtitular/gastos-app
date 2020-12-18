from pydantic import BaseModel

class tipo_token(BaseModel):
    id: int
    nombre: str
    tiene_vigencia: bool