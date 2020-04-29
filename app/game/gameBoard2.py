import numpy as np

np.set_printoptions(linewidth=400)

from app.models.coord import Coord
from app.models.game import Game

from app.game.board import Board
from app.game.gameSnake import GameSnake, directionFromTo

class GameBoard:
    def __init__(self, data: Game):
        verbose = False
        self.theMove = ( 'right', 'default' )
        limit = 6
        width = data.board.width
        height = data.board.height
        snakeCount = len(data.board.snakes)
        board = Board(width, height, snakeCount)
        for c in data.board.food:
            board.set(c.x, c.y, 0, 'F')
        snakes = []
        for i, sData in enumerate(data.board.snakes):
            bodyPoints = []
            for c in sData.body:
                bodyPoints.append( (c.x, c.y) )
            if verbose:
                print(bodyPoints)
            snake = GameSnake(sData.id, i+1, bodyPoints)
            snake.addBodyToBoard(board)
            snakes.append(snake)
        print(board)
        for snake in snakes:
            snake.floodHead(board, limit)

        mySnake = snakes[0]

        mySnake.analyze(board, snakes)
        move = mySnake.move
        shout = mySnake.move
        if move != None:
            self.theMove = (move, shout)
        print(mySnake)
        print(board)


    def getMoveShout(self):
        return self.theMove

    def emptyBoard(self):
        return self.board.copy()
