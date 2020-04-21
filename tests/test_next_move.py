import json
from app.models.models import Coord
from app.models.board import Board
from app.models.snake import Snake
from jsonData import getBoardJson


def createBoard():
    boardJS = getBoardJson()
    return Board(**json.loads(boardJS))

class TestMove:

    def test_possibleMoveTiles(self):
        board = createBoard()
        snake = board.snakes[1]
        validNext = snake.possibleMoveTiles(board)
        expected = [Coord(x=2, y=3), Coord(x=3, y=2)]
        print('validNext')
        print(validNext)
        print('expected')
        print(expected)
        print(snake.shout)
        assert validNext == expected
        #assert False

    def test_nextMove(self):
        board = createBoard()
        snake = board.snakes[1]
        validNext = snake.possibleMoveTiles(board)
        nextMove = board.selectTile(validNext)
        ## TODO when nextMove improves replace following
        expected = validNext[0]
        print('nextMove')
        print(nextMove)
        print('expected')
        print(expected)
        print(snake.shout)
        assert nextMove == expected
        #assert False
