import json
from pathlib import Path
from timeit import default_timer as timer
from threading import Timer

from app.models.game import Game
from app.models.coord import Coord

def _storeGameStep(game: Game):
    Path("games").mkdir(parents=True, exist_ok=True)
    gameJSON = json.dumps(game.dict())
    fileName = Path("games/" + game.getId())
    with open(fileName, "a") as gameFile:
        gameFile.write(gameJSON)

def startGame(game: Game):
    print('start with game', game)
    _storeGameStep(game)
    headType = 'bwc-earmuffs'
    tailType = 'bwc-ice-skate'
    color = "#add8e6"
    response = {"color": color, "headType": headType, "tailType": tailType}
    return response


def _finishMove(game, head, validNext, nextMove, direction):
    print('finish move after delay' +str(game))
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
