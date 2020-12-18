
from pydantic import BaseModel

class informacion_contacto(BaseModel):
    id: int
    persona: persona
    movil: str
    direccion: str
    mail: str
    