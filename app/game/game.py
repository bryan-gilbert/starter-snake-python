from timeit import default_timer as timer
from threading import Timer

from app.config.config import redisConnection
from app.models.game import Game
from app.models.coord import Coord
from app.game.gameBoard2 import GameBoard


gameStore = {}

def _storeGameStep(game: Game):
    id = game.getId()
    str = json.dumps(game.dict())
    try:
        redisConnection.set(id,str)
    except:
        # sometimes the connection is reset and throws a redis.exceptions.ConnectionError
        pass

def getGame(id):
    data = redisConnection.get(id)
    print('Read game {} from redis store'.format(id))
    print(data)
    return data

def startGame(game: Game):
    print("start game: " + game.game.id)
    print("start turn: " + str(game.turn))
    print('start with game', game)
    _storeGameStep(game)
    headType = 'evil'
    tailType = 'flecked'
    color = "#add8e6"
    response = {"color": color, "headType": headType, "tailType": tailType}
    return response


def _finishMove(game, move = '', elapsedTime = 0):
    _storeGameStep(game)

def moveGame(game: Game):
    start = timer()
    board = GameBoard(game)
    move = board.theMove
    end = timer()
    elapsedTime = end - start
    print("move game: " + game.game.id)
    print("move turn: " + str(game.turn))
    print("move time: " + str(elapsedTime)) # Time in seconds
    print("move results", move)
    #Timer(0.1, _finishMove, [game, move, elapsedTime]).start()
    return {"move": move[0], "shout": move[1] }

def endGame(game: Game):
    print("end game: " + game.game.id)
    print("end turn: " + str(game.turn))
    print('end with game', game)
    _storeGameStep(game)
    return {}
