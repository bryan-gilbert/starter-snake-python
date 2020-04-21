import json
from app.models.game import  Game
from app.models.coord import Coord
from app.models.board import Board
from app.models.snake import Snake

from jsonData import getBoardJson

def createSnake():
    """ helper function makes a snake """
    return Snake(id='id', name='snake', health=100, body=[], shout='')

def createBoard():
    boardJS = getBoardJson()
    return Board(**json.loads(boardJS))


class TestBoard:

    def test_board(self):
        dim = 11
        board = Board(height = dim, width = dim, food=[], snakes=[])
        assert board.width == dim
        assert board.height == dim
        assert board.inBounds(Coord(x=0,y=0))
        assert board.inBounds(Coord(x=dim-1,y=dim-1))
        assert board.inBounds(Coord(x=dim,y=dim+1)) == False
        assert board.inBounds(Coord(x=-1,y=dim)) == False

    def test_direction_down(self):
        c1 = Coord(x=5,y=5)
        c2 = Coord(x=c1.x, y=c1.y+1)
        direction = Coord.directionFromTo(c1,c2)
        assert direction == 'down'

    def test_direction_up(self):
        c1 = Coord(x=5,y=5)
        c2 = Coord(x=c1.x, y=c1.y-1)
        direction = Coord.directionFromTo(c1,c2)
        assert direction == 'up'

    def test_direction_right(self):
        c1 = Coord(x=5,y=5)
        c2 = Coord(x=c1.x+1, y=c1.y)
        direction = Coord.directionFromTo(c1,c2)
        assert direction == 'right'

    def test_direction_left(self):
        c1 = Coord(x=5,y=5)
        c2 = Coord(x=c1.x-1, y=c1.y)
        direction = Coord.directionFromTo(c1,c2)
        assert direction == 'left'

    def test_avoidBodyParts(self):
        board = createBoard()
        expected = [Coord(x=4, y=1), Coord(x=3, y=1), Coord(x=2, y=1), Coord(x=2, y=2), Coord(x=1, y=2), Coord(x=0, y=2), Coord(x=1, y=3), Coord(x=0, y=3), Coord(x=3, y=3), Coord(x=3, y=4), Coord(x=3, y=5), Coord(x=3, y=6), Coord(x=3, y=7), Coord(x=6, y=5), Coord(x=5, y=5), Coord(x=4, y=5), Coord(x=4, y=6), Coord(x=4, y=4), Coord(x=4, y=8), Coord(x=1, y=8), Coord(x=1, y=9)]
        avoid = board.getBodyParts()
        print('avoid')
        print(avoid)
        print('expected')
        print(expected)
        assert avoid == expected

    def test_avoidDangerZones(self):
        board = createBoard()
        board.snakes = []

        # create first snake is shorter thant middle
        smaller = createSnake()
        smaller.id='smaller'
        dx = 5
        dy = 2
        smaller.body= [Coord(x=dx, y=dy), Coord(x=dx+1, y=dy)]
        board.snakes.append(smaller)

        # create target snake
        target = createSnake()
        target.id='target'
        dx = 2
        dy = 2
        target.body= [Coord(x=dx, y=dy), Coord(x=dx+1, y=dy), Coord(x=dx+2, y=dy)]
        board.snakes.append(target)

        # create last snake is same size as target snake and is to be avoided
        sameSize = createSnake()
        sameSize.id = 'sameSize'
        dx = 7
        dy = 2
        sameSize.body= [Coord(x=dx, y=dy), Coord(x=dx, y=dy+1), Coord(x=dx, y=dy+2)]
        board.snakes.append(sameSize)

        expected = sameSize.validNextTiles(board)

        avoid = board.getDangerZones(target)
        print('avoid')
        print(avoid)
        print('expected')
        print(expected)
        assert avoid == expected

