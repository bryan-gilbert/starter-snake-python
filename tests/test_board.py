import json
from app.models.models import Board, Coord, Game, Snake
from jsonData import getGameJson, getBoardJson, getSnakeJson

class TestBoard:

    def test_board(self):
        dim = 11
        board = Board(height = dim, width = dim, food=[], snakes=[])
        assert board.width == dim
        assert board.height == dim
        assert board.inBounds(Coord(x=0,y=0))
        assert board.inBounds(Coord(x=dim,y=dim))
        assert board.inBounds(Coord(x=dim,y=dim+1)) == False
        assert board.inBounds(Coord(x=-1,y=dim)) == False

    def test_boardFromJson(self):
        boardJS = getBoardJson()
        board = Board(**json.loads(boardJS))
        assert board.width == 11


class TestGame:

    def test_gameFromJson(self):
        gameJSON = getGameJson()
        game = Game(**json.loads(gameJSON))
        assert game.board.width == 11
        assert game.you.health == 100
        assert game.you.body[0] == Coord(x=9, y=1)


class TestSnake:

    boardJSON = getBoardJson()
    board = Board(**json.loads(boardJSON))

    def createSnake(self):
        snakeJSON = getSnakeJson()
        snake = Snake(**json.loads(snakeJSON))
        return snake


    def test_nextValid_inBoard(self):
        snake = self.createSnake()
        dx = 1
        dy = 1
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy+1)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=1, y=0), Coord(x=0, y=1), Coord(x=2, y=1)]

    def test_nextValid_origin(self):
        snake = self.createSnake()
        dx = 0
        dy = 0
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy+1)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=1, y=0)]

    def test_nextValid_farRight(self):
        snake = self.createSnake()
        dx = 11
        dy = 0
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy+1)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=10, y=0)]

    def test_nextValid_bottomRight(self):
        snake = self.createSnake()
        dx = 11
        dy = 11
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy-1)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=10, y=11)]

    def test_nextValid_bottomRight2(self):
        snake = self.createSnake()
        dx = 11
        dy = 11
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx-1,y=dy)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=11, y=10)]

    def test_nextValid_bottomLeft(self):
        snake = self.createSnake()
        dx = 11
        dy = 11
        # body pointing down
        snake.body = [Coord(x=0,y=dy), Coord(x=0,y=dy-1)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=1, y=dy)]
