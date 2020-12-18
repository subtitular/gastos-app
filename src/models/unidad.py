from pydantic import BaseModel
from enum import Enum

class unidad(BaseModel,Enum):
    HORA = 1
    DIA = 2
    SEMANA = 3
    MES = 4
    BIMESTRE = 5
    TRIMESTRE = 6
    SEMESTRE = 7
    ANUAL = 8
    

