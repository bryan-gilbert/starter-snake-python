
from fastapi import FastAPI, Request
import uvicorn

from app.game.game import endGame, moveGame, startGame, getGame
from app.models.game import Game
from app.config.config import redisConnection


app = FastAPI()

@app.get('/')
def index():
    return {"name": 'zombie snake', "description":'''
This is a Zombie Snake.
Battlesnake documentation can be found at
<a href="https://docs.battlesnake.com">https://docs.battlesnake.com</a>.
'''}

@app.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return {"ping":"true"}

@app.post('/start')
async def start(data: Game, request: Request):
    raw = await request.json()
    return startGame(data, raw)

@app.post('/move')
async def move(data: Game, request: Request):
    raw = await request.json()
    return moveGame(data, raw)

@app.post('/end')
async def end(data: Game, request: Request):
    raw = await request.json()
    return endGame(data, raw)


@app.get('/game/{game_id}')
def getGame(game_id: str):
    return getGame(game_id)


# You should use uvicorn to run the app locally.  __main__ is provided to run it in a debugger. See
# https://fastapi.tiangolo.com/tutorial/debugging/
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
