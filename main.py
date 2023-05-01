from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.player import player_router
from routers.user import user_router

app = FastAPI()
app.title = 'Argentina campeao do mundo'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)
app.include_router(player_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


players = [
    {
        'id': 23,
        'nombre': 'Emiliano Martinez',
        'edad': 30,
        'apodo': 'Dibujo, Boceto',
        'puesto': 'Arquero',
        'equipo': 'Aston Villa'
    },
    {
        'id': 10,
        'nombre': 'Lionel Andres Messi',
        'edad': 35,
        'apodo': 'Pulga, GOAT',
        'puesto': 'de Messi',
        'equipo': 'PSG'
    },
    {
        'id': 13,
        'nombre': 'Cristian Romero',
        'edad': 24,
        'apodo': 'Cuti, Cuttie',
        'puesto': 'Defensor Central',
        'equipo': 'Tottenham'
    },
    {
        'id': 19,
        'nombre': 'Nicolas Otamendi',
        'edad': 35,
        'apodo': 'Centinela, General',
        'puesto': 'Defensor Central',
        'equipo': 'Benfica'
    },
]

@app.get("/", tags=["Doc del campeon"])
def home():
    return HTMLResponse( """
    <h1>Campeones del mundo, por tercera vez</h1>
    <p>Si esto no es el futbol, el futbol donde está</p>
    """)


