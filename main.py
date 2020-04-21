
from fastapi import Body, FastAPI
import uvicorn

from app.game.game import endGame, moveGame, startGame
from app.models.game import Game

app = FastAPI()

@app.get('/')
def index():
    return '''
This is a Zombie Snake.
Battlesnake documentation can be found at
<a href="https://docs.battlesnake.com">https://docs.battlesnake.com</a>.
'''

@app.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return {"ping":"true"}

@app.post('/start')
def start(data: Game):
    return startGame(data)

@app.post('/move')
def move(data: Game):
    return moveGame(data)

@app.post('/end')
def end(data: Game):
    return endGame(data)

# You should use uvicorn to run the app locally.  __main__ is provided to run it in a debugger. See
# https://fastapi.tiangolo.com/tutorial/debugging/
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
