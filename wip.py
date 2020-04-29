from app.models.coord import Coord

from app.game.v3.board import Board, EMPTY
from app.game.v3.gameSnake import GameSnake, directionFromTo
from app.game.v3.gameBoard import GameBoard

width = 11
height = 11
count = 3

def createBoard():
    board = Board(width, height, count)
    board.set(1,2,0,'F')
    return board


def testBoard():
    board = createBoard()
    #board.printBoard('test print board')
    v = board.get(3,4,0)
    assert(v == EMPTY)
    pts = [(0,0), (height-1,width-1)]
    # print('Should be all true')
    for p in pts:
        assert(board.inBounds(p[0],p[1]))
    pts = [(-1,0), (0,-1), (height-1,width), (height,width-1)]
    # print('Should be all false')
    for p in pts:
        assert( not board.inBounds(p[0],p[1]))

    h = height
    w = width
    assert(board.getFourLegalPoints(0,0) == [(0, 1), (1, 0)])
    assert(board.getFourLegalPoints(5,5) == [(5, 4), (5, 6), (4, 5), (6, 5)])
    assert(board.getFourLegalPoints(w-1,h-1) == [(w-1, h-2), (w-2, h-1)])


def testCoord():
    c1 = Coord(x=2,y=3)
    c2 = Coord(x=3,y=3)
    print(c1, c2)
    print(Coord.directionFromTo(c1,c2))

def testSnake():
    board = createBoard()
    body = [(3,3), (3,4), (4,4), (4,5)]
    snake = GameSnake('someId', 1, body)
    snake.addBodyToBoard(board)
    snake.floodHead(board, 3)
    v = board.get(3,3,1)
    assert(v == 'Z')
    v = board.get(3,4,1)
    assert(v == 'Y')
    v = board.get(4,4,1)
    assert(v == 'X')
    v = board.get(3,2,1)
    assert(v == 'a')
    # print(board)

def test2Snakes(body1, body2, verbose):
    board = createBoard()
    snake1 = GameSnake('someId', 1, body1)
    snake1.addBodyToBoard(board)
    snake2 = GameSnake('otherId', 2, body2)
    snake2.addBodyToBoard(board)
    # print(board)
    limit = 6
    snake1.floodHead(board, limit)
    snake2.floodHead(board, limit)
    snake1.analyze(board)
    if verbose:
        print(board, [snake1, snake2])
    return snake1

def test2SnakesA(verbose):
    body1 = [(3,3), (3,4), (4,4), (4,5)]
    y = 3
    x = 5
    body2 = [(x,y), (x,y+1), (x+1,y+1), (x+2,y+1)]
    snake1 = test2Snakes(body1, body2, verbose)
    print(snake1)

def testNSnakes(snakeBodies, verbose):
    limit = 6
    board = createBoard()
    snakes = []
    for i, body in enumerate(snakeBodies):
        snake = GameSnake('someId{}'.format(i+1), i+1, body)
        snake.addBodyToBoard(board)
        snakes.append(snake)
    if verbose:
        print(board)
    for snake in snakes:
        snake.floodHead(board, limit)

    snakes[0].analyze(board, snakes)
    if verbose:
        print(board)
    return snakes[0]

def test4Snakes(verbose):
    body1 = [(3,3), (3,4), (4,4), (4,5)]
    y = 3
    x = 5
    body2 = [(x,y), (x,y+1), (x+1,y+1), (x+2,y+1)]
    # add a third snake that is to the right of our and smaller. Therefore our snake should not avoid this one!
    y = 3
    x = 1
    body3 = [(x,y), (x,y+1), (x-1,y+1)]
    snake1 = testNSnakes([body1, body2, body3], verbose)
    print(snake1)


def testDirectionFromTo():
    c1 = (3,4)
    board = createBoard()
    four = board.getFourLegalPoints(c1[0], c1[1])
    assert('up' == directionFromTo(c1,four[0]))
    assert('down' == directionFromTo(c1,four[1]))
    assert('left' == directionFromTo(c1,four[2]))
    assert('right' == directionFromTo(c1,four[3]))


def main():
    verbose = False
    testBoard()
    testDirectionFromTo()
    testSnake()
    verbose = True
    #test2SnakesA(verbose)
    test4Snakes(verbose)

if __name__=="__main__":
    main()