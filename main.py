import json
import os
import random
from fastapi import Body, FastAPI
import uvicorn

from app.game.start import startGame
from app.game.move import moveSimple, moveBest, moveGame
from app.models.models import Game

app = FastAPI()


@app.get('/')
def index():
    return '''
This is Zombie Snake.
Battlesnake documentation can be found at
<a href="https://docs.battlesnake.com">https://docs.battlesnake.com</a>.
'''

@app.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return {"success":"true"}


@app.post('/start')
def start(data: Game):
    return startGame(data)

#def start(data = Body(...)):
#    return startGame(data)

@app.post('/move')
def move(data: Game):
    return moveGame(data)


@app.post('/end')
def end(data = Body(...)):
    print("end data: " + json.dumps(data))
    return {}

# You should use uvicorn to run the app locally.  __main__ is provided to run it in a debugger. See
# https://fastapi.tiangolo.com/tutorial/debugging/
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
