import json
from pathlib import Path
from timeit import default_timer as timer
from threading import Timer

from app.config.config import redisConnection
from app.models.game import Game
from app.models.coord import Coord
from app.game.gameBoard import GameBoard

from app.config.config import redisConnection
from app.models.game import Game
from app.models.coord import Coord
from app.game.storage import Storage


def startGame(game: Game, raw, storage: Storage):
    print('start with game', game)
    storage.storeGameStep(raw, game, 0, {}, None)
    headType = 'evil'
    tailType = 'flecked'
    color = "#add8e6"
    response = {"color": color, "headType": headType, "tailType": tailType}
    return response


def moveGame(game: Game, raw, startTime, storage: Storage):
    print('game id "{}" and turn {}'.format(game.game.id, game.turn))
    gameBoard = GameBoard(game)
    moveShout = gameBoard.getMoveShout()
    results = {"move": moveShout[0], "shout": moveShout[1] }
    def _store(raw, game, elapsed, results, gameBoard):
        storage.storeGameStep(raw, game, elapsed, results, gameBoard)
    endTime = timer()
    elapsedTime = endTime - startTime
    Timer(0.1, _store, [raw, game, elapsedTime, results, gameBoard]).start()
    return results


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


def _finishMove(game, gameBoard = None, move = '', elapsedTime = 0):
    print("store game: " + game.game.id)
    print("store turn: " + str(game.turn))
    print("store move: ",  move)
    print("store time: ",  elapsedTime)
    _storeGameStep(game, gameBoard)

def moveGame(game: Game):
    start = timer()
    gameBoard = TheGame(game)
    move = gameBoard.getMove()
    end = timer()
    elapsedTime = end - start
    print("move time: " + str(elapsedTime)) # Time in seconds
    #Timer(0.1, _finishMove, [game, gameBoard, move, elapsedTime]).start()
    return {"move": move[0], "shout": move[1] }

def endGame(game: Game):
    print('end with game', game)
    #_storeGameStep(game)
    return {}