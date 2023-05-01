from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.player import Player as PlayerModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.player import PlayerService
from schemas.player import Player

player_router = APIRouter()



@player_router.get('/players', tags=['Jugadores'], response_model=List[Player], status_code=200, dependencies=[Depends(JWTBearer())])
def get_players() -> List[Player]:
    db = Session()
    result = PlayerService(db).get_players()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@player_router.get('/players/{id}', tags=['Jugadores'], response_model=Player, status_code=200)
def get_player(id: int = Path(ge=1, le=1000)) -> Player:
    db = Session()
    result = PlayerService(db).get_player(id)
    if not result:
        return JSONResponse(status_code=404, content={'message':'There is no player with such id'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@player_router.get('/players/', tags=['Jugadores'], response_model=List[Player], status_code=200)
def get_players_by_position(position: str = Query(min_length=5, max_length=20)) -> List[Player]:
    db = Session()
    result = PlayerService(db).get_players_by_position(position)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@player_router.post('/players', tags=['Jugadores'], response_model=dict, status_code=201)
def create_player(player: Player) -> dict:
    db = Session()
    PlayerService(db).create_player(player)
    return JSONResponse(status_code=201, content={'message': 'Jugador incluido'})

@player_router.put('/players/{id}', tags=['Actualizar datos de jugadores'],response_model=dict, status_code=200)
def update_player(id: int, player: Player) -> dict:
    db = Session()
    result = PlayerService(db).get_player(id)
    if not result:
        return JSONResponse(status_code=404, content={'message':'There is no player with such id'})
    
    PlayerService(db).update_player(id, player)
    return JSONResponse(status_code=200, content={'message': 'Jugador modificado'})

@player_router.delete('/players/{id}', tags=['Eliminar jugadores'], response_model=dict, status_code=200)
def delete_player(id: int) -> dict:
    db = Session()
    result = db.query(PlayerModel).filter(PlayerModel.id == id).first()
    if not result:
            return JSONResponse(status_code=404, content={'message':'There is no player with such id'})

    PlayerService(db).delete_player(id)
    return JSONResponse(status_code=200, content={'message': 'Jugador eliminado'})