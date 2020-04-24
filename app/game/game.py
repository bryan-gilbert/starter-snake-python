import json
from pathlib import Path
from timeit import default_timer as timer
from threading import Timer

from app.config.config import redisConnection
from app.models.game import Game
from app.models.coord import Coord
from app.game.gameBoard import GameBoard

from app.game.gameBoard import GameBoard

class TheGame:
    def __init__(self, game: Game):
        self.board = GameBoard(game)

    def getMove(self):
        return self.board.theMove


gameStore = {}

def _storeGameStepOld(game: Game):
    id = game.getId()
    if not id in gameStore:
        gameStore[id] = []
    list = gameStore[id]
    if not list:
        gameStore[id] = []
        list = gameStore[id]
    list.append(game)

def _storeGameStep(game: Game, gameBoard: GameBoard):
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
    print('start with game', game)
    _storeGameStep(game)
    headType = 'evil'
    tailType = 'flecked'
    color = "#add8e6"
    response = {"color": color, "headType": headType, "tailType": tailType}
    return response


def _finishMove(game, gameBoard, direction):
    print("move game: " + game.game.id)
    print("move turn: " + str(game.turn))
    print("move direction: " + direction)
    _storeGameStep(game, gameBoard)

def moveGame(game: Game):
    start = timer()
    gameBoard = TheGame(game)
    direction = gameBoard.getMove()
    end = timer()
    print("move time: " + str(end - start)) # Time in seconds
    Timer(0.1, _finishMove, [game, gameBoard, direction]).start()
    return {"move": direction }

def old():
    board = game.board
    snake = game.you
    head = snake.body[0]
    validNext = snake.possibleMoveTiles(board)
    nextMove = board.selectTile(validNext)
    direction = Coord.directionFromTo(head,nextMove)
    end = timer()
    print("move time: " + str(end - start)) # Time in seconds
    Timer(0.1, _finishMove, [game, head, validNext, nextMove, direction]).start()
    return {"move": direction }

def endGame(game: Game):
    print('end with game', game)
    _storeGameStep(game)
    return {}
