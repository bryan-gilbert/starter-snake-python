import json
from timeit import default_timer as timer
from threading import Timer

from app.config.config import redisConnection
from app.models.game import Game
from app.models.coord import Coord
from app.game.gameBoard2 import GameBoard


from pydantic import BaseModel, Json
from typing import List

gameStore = {}

class MoveData(BaseModel):
    turn: int
    move: str
    elapsed: int
    raw: Json

class GameData(BaseModel):
    id: str
    moves: List[MoveData]

def _storeGameStep(game: Game, raw, move = ('',''), elapsed = 0):
    id = game.getId()
    if not id in gameStore:
        gameDict = GameData(id = id, moves = [])
        gameStore[id] = gameDict

    gameDict: GameData = gameStore[id]
    moveJson = json.dumps(raw)
    direction = move[0]
    # print('create MoveData from ', game.turn, direction, elapsed, moveJson)
    move = MoveData(turn = game.turn, move = direction, elapsed = elapsed, raw = moveJson)
    gameDict.moves.append(move)

    str = json.dumps(gameDict.json())
    try:
        redisConnection.set(id, str)
    except:
        # sometimes the connection is reset and throws a redis.exceptions.ConnectionError
        pass

def getGame(id):
    data = redisConnection.get(id)
    print('Read game {} from redis store'.format(id))
    print(data)
    return data

def startGame(game: Game, raw):
    print("start game: " + game.game.id)
    print("start turn: " + str(game.turn))
    print('start with raw', raw)
    _storeGameStep(game, raw)
    headType = 'shac-caffeine'  # 'smile'
    tailType = 'freckled'
    color = "#e26d30"            # "#add8e6"
    response = {"color": color, "headType": headType, "tailType": tailType}
    return response


def _finishMove(game, raw, move = '', elapsedTime = 0):
    _storeGameStep(game, raw, move, elapsedTime)

def moveGame(game: Game, raw):
    print('Move with raw', raw)
    start = timer()
    board = GameBoard(game)
    move = board.theMove
    end = timer()
    elapsedTime = end - start
    print("move game: " + game.game.id)
    print("move turn: " + str(game.turn))
    print("move time: " + str(elapsedTime)) # Time in seconds
    print("move results", move)
    Timer(0.1, _finishMove, [game, raw, move, elapsedTime]).start()
    return {"move": move[0], "shout": move[1] }

def endGame(game: Game, raw):
    print("end game: " + game.game.id)
    print("end turn: " + str(game.turn))
    print('end with raw', raw)
    _storeGameStep(game, raw)
    return {}
