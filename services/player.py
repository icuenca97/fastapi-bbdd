from models.player import Player as PlayerModel
from schemas.player import Player
from fastapi.responses import JSONResponse


class PlayerService():

    def __init__(self, db) -> None:
        self.db = db

    def get_players(self):
        result = self.db.query(PlayerModel).all()
        return result

    def get_player(self, id):
        result = self.db.query(PlayerModel).filter(PlayerModel.id == id).first()
        return result

    def get_players_by_position(self, position):
        result = self.db.query(PlayerModel).filter(PlayerModel.puesto == position).all()
        return result

    def create_player(self, player: Player):
        new_player = PlayerModel(**player.dict())
        self.db.add(new_player)
        self.db.commit()
        return
    
    def update_player(self, id: int, data: Player):
        player = self.db.query(PlayerModel).filter(PlayerModel.id == id).first()
        
        player.nombre = data.nombre
        player.edad = data.edad
        player.apodo = data.apodo
        player.puesto = data.puesto
        player.equipo = data.equipo

        self.db.commit()
        return

    def delete_player(self, id: int):
        

        self.db.query(PlayerModel).filter(PlayerModel.id == id).delete()
        self.db.commit()
        return