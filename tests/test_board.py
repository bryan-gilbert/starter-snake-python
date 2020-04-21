import json
from app.models.models import directionFromTo, Board, Coord, Game, Snake
from jsonData import getGameJson, getBoardJson, getSnakeJson

def createSnake():
    """ helper function makes a snake """
    snakeJSON = getSnakeJson()
    return Snake(**json.loads(snakeJSON))

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
        assert board.inBounds(Coord(x=dim,y=dim))
        assert board.inBounds(Coord(x=dim,y=dim+1)) == False
        assert board.inBounds(Coord(x=-1,y=dim)) == False

    def test_direction_down(self):
        c1 = Coord(x=5,y=5)
        c2 = Coord(x=c1.x, y=c1.y+1)
        direction = directionFromTo(c1,c2)
        assert direction == 'down'

    def test_direction_up(self):
        c1 = Coord(x=5,y=5)
        c2 = Coord(x=c1.x, y=c1.y-1)
        direction = directionFromTo(c1,c2)
        assert direction == 'up'

    def test_direction_right(self):
        c1 = Coord(x=5,y=5)
        c2 = Coord(x=c1.x+1, y=c1.y)
        direction = directionFromTo(c1,c2)
        assert direction == 'right'

    def test_direction_left(self):
        c1 = Coord(x=5,y=5)
        c2 = Coord(x=c1.x-1, y=c1.y)
        direction = directionFromTo(c1,c2)
        assert direction == 'left'

    def test_avoidBodyParts(self):
        board = createBoard()
        expected = [Coord(x=4, y=1), Coord(x=3, y=1), Coord(x=2, y=1), Coord(x=2, y=2), Coord(x=1, y=2), Coord(x=0, y=2), Coord(x=1, y=3), Coord(x=0, y=3), Coord(x=3, y=3), Coord(x=3, y=4), Coord(x=3, y=5), Coord(x=3, y=6), Coord(x=6, y=5), Coord(x=5, y=5), Coord(x=4, y=5)]
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


class TestGame:

    def test_gameFromJson(self):
        gameJSON = getGameJson()
        game = Game(**json.loads(gameJSON))
        assert game.board.width == 11
        assert game.you.health == 100
        assert game.you.body[0] == Coord(x=9, y=1)


class TestSnake:

    board = createBoard()

    def test_nextValid_inBoard(self):
        snake = createSnake()
        dx = 1
        dy = 1
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy+1)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=1, y=0), Coord(x=0, y=1), Coord(x=2, y=1)]

    def test_nextValid_origin(self):
        snake = createSnake()
        dx = 0
        dy = 0
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy+1)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=1, y=0)]

    def test_nextValid_farRight(self):
        snake = createSnake()
        dx = 11
        dy = 0
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy+1)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=10, y=0)]

    def test_nextValid_bottomRight(self):
        snake = createSnake()
        dx = 11
        dy = 11
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx,y=dy-1)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=10, y=11)]

    def test_nextValid_bottomRight2(self):
        snake = createSnake()
        dx = 11
        dy = 11
        snake.body = [Coord(x=dx,y=dy), Coord(x=dx-1,y=dy)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=11, y=10)]

    def test_nextValid_bottomLeft(self):
        snake = createSnake()
        dx = 11
        dy = 11
        # body pointing down
        snake.body = [Coord(x=0,y=dy), Coord(x=0,y=dy-1)]
        validNext = snake.validNextTiles(self.board)
        print(validNext)
        assert validNext == [Coord(x=1, y=dy)]


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
