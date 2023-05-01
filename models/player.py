from config.database import Base
from sqlalchemy import Column, Integer, String

class Player(Base):

    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)
    apodo = Column(String)
    puesto = Column(String)
    equipo = Column(String)
