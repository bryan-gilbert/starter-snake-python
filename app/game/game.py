import json
from timeit import default_timer as timer
from threading import Timer

from app.models.game import Game
from app.models.coord import Coord

gameStore = {}

def _storeGameStep(game: Game):
    id = game.getId()
    if not id in gameStore:
        gameStore[id] = []
    list = gameStore[id]
    list.append(game)

def getGame(id):
    data = gameStore[id]
    print(data)
    return data

def startGame(game: Game):
    print('start with game', game)
    _storeGameStep(game)
    headType = 'bwc-earmuffs'
    tailType = 'bwc-ice-skate'
    color = "#add8e6"
    response = {"color": color, "headType": headType, "tailType": tailType}
    return response


def _finishMove(game, head, validNext, nextMove, direction):
    print("move game: " + game.game.id)
    print("move turn: " + str(game.turn))
    print("move head: " + str(head))
    print("move next: " + str(validNext))
    print("move move: " + str(nextMove))
    print("move direction: " + direction)
    _storeGameStep(game)

def moveGame(game: Game):
    start = timer()
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
