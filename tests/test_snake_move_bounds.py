import json
from app.models.models import Board, Coord, Snake
from jsonData import getBoardJson

def createSnake():
    """ helper function makes a snake """
    return Snake(id='id', name='snake', health=100, body=[], shout='')

def createBoard():
    boardJS = getBoardJson()
    return Board(**json.loads(boardJS))

class TestSnakeMoveBounds:

    board = createBoard()
    maxX = board.width - 1
    maxY = board.height - 1

    def test_nextValid_inBoard(self):
        snake = createSnake()
        dx = 1
        dy = 1
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy+1)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=dx, y=dy-1), Coord(x=dx-1, y=dy), Coord(x=dx+1, y=dy)]

    def test_nextValid_origin_up(self):
        snake = createSnake()
        dx = 0
        dy = 0
        # body pointing up at top left corner of board
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy+1)]
        validNext = snake.validNextTiles(self.board)
        print(snake.body)
        print(validNext)
        assert validNext == [Coord(x=dx+1, y=dy)]

    def test_nextValid_origin_left(self):
        snake = createSnake()
        dx = 0
        dy = 0
        # body pointing left at top left corner of board
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx+1,y=dy)]
        validNext = snake.validNextTiles(self.board)
        print(snake.body)
        print(validNext)
        assert validNext == [Coord(x=dx, y=dy+1)]

    def test_nextValid_topRight_up(self):
        snake = createSnake()
        dx = self.maxX
        dy = 0
        # body pointing up right at top right corner of board
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy+1)]
        validNext = snake.validNextTiles(self.board)
        print(snake.body)
        print(validNext)
        assert validNext == [Coord(x=dx-1, y=dy)]

    def test_nextValid_topRight_right(self):
        snake = createSnake()
        dx = self.maxX
        dy = 0
        # body pointing right at top right corner of board
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx-1,y=dy)]
        validNext = snake.validNextTiles(self.board)
        print(snake.body)
        print(validNext)
        assert validNext == [Coord(x=dx, y=dy+1)]

    def test_nextValid_bottomLeft_left(self):
        snake = createSnake()
        dx = 0
        dy = self.maxY
        # body pointing left at bottom left corner of board
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx+1,y=dy)]
        validNext = snake.validNextTiles(self.board)
        print(snake.body)
        print(validNext)
        assert validNext == [Coord(x=dx, y=dy-1)]

    def test_nextValid_bottomLeft_down(self):
        snake = createSnake()
        dx = 0
        dy = self.maxY
        # body pointing down at bottom left corner of board
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy-1)]
        validNext = snake.validNextTiles(self.board)
        print(snake.body)
        print(validNext)
        assert validNext == [Coord(x=dx+1, y=dy)]

    def test_nextValid_bottomRight_right(self):
        snake = createSnake()
        dx = self.maxX
        dy = self.maxY
        # body pointing right at bottom right corner of board
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx-1,y=dy)]
        validNext = snake.validNextTiles(self.board)
        print(snake.body)
        print(validNext)
        assert validNext == [Coord(x=dx, y=dy-1)]

    def test_nextValid_bottomRight_down(self):
        snake = createSnake()
        dx = self.maxX
        dy = self.maxY
        # body pointing down at bottom right corner of board
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy-1)]
        validNext = snake.validNextTiles(self.board)
        print(snake.body)
        print(validNext)
        assert validNext == [Coord(x=dx-1, y=dy)]