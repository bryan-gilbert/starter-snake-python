from timeit import default_timer as timer

from app.models.game import Game
from app.models.coord import Coord

def moveGame(game: Game):
    start = timer()
    board = game.board
    snake = game.you
    head = snake.body[0]
    validNext = snake.possibleMoveTiles(board)
    nextMove = board.selectTile(validNext)
    direction = Coord.directionFromTo(head,nextMove)
    print("move game: " + game.game.id)
    print("move turn: " + str(game.turn))
    print("move head: " + str(head))
    print("move next: " + str(validNext))
    print("move move: " + str(nextMove))
    print("move direction: " + direction)
    end = timer()
    print("move time: " + str(end - start)) # Time in seconds
    return {"move": direction }
