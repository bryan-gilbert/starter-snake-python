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

        # load the food into the board
        for c in data.board.food:
            board.set(c.x, c.y, 0, '*')

        def _createSnake(snakeData, index):
            bodyPoints = []
            for c in snakeData.body:
                bodyPoints.append( (c.x, c.y) )
            snake = GameSnake(snakeData.id, snakeData.health, index, bodyPoints)
            return snake

        # find my snake and collect the rest into a list
        dataSnakes = []
        mySnakeId = data.you.id
        indices = [i for i, s in enumerate(data.board.snakes) if s.id == mySnakeId]
        mySnakeIndex = indices[0]
        dataSnakes.append(data.board.snakes.pop(indices[0]))
        dataSnakes.extend(data.board.snakes)

        # create the data snakes
        snakes = []
        for i, sData in enumerate(dataSnakes):
            snake = _createSnake(sData, i+1)
            snakes.append(snake)

        for snake in snakes:
            snake.addBodyToBoard(board)
        print(board)

        for snake in snakes:
            snake.floodHead(board, limit)
            
        mySnake = snakes[0]
        mySnake.analyze(board, snakes)
        move = mySnake.move
        shout = mySnake.move
        if move != None:
            self.theMove = (move, shout)
        print(board)
        print(mySnake)


    def getMoveShout(self):
        return self.theMove

    def emptyBoard(self):
        return self.board.copy()
