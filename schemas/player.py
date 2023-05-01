from pydantic import BaseModel, Field
from typing import Optional


class Player(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(max_length=30)
    edad: int = Field(le=40)
    apodo: str = Field(max_length=30)
    puesto: str = Field(max_length=20)
    equipo: str = Field(max_length=20)

    class Config:
        schema_extra = {
            "example": {
                'id': 0,
                'nombre': 'Jugador ejemplo',
                'edad': 21,
                'apodo': 'Apodo del jugador',
                'puesto': 'Posicion en la cancha',
                'equipo': 'Equipo actual'
            }
        }
