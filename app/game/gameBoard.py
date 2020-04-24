import numpy as np
import random

from app.models.coord import Coord
from app.models.snake import Snake
from app.models.board import Board
from app.models.game import Game

def directionFromTo(c1: Coord, c2: Coord):
    """ c1 is the "from" tile and c2 is the "to" tile """
    direction = ''
    assert c1 != c2
    if c2.x > c1.x:
        direction = 'right'
    elif c2.x < c1.x:
        direction = 'left'
    elif c2.y > c1.y:
        direction = 'down'
    else:
        direction = 'up'
    return direction

class Bounds:
    def __init__(self, w, h):
        self.w = w - 1
        self.h = h - 1

    def getFourLegalPoints(self, c: Coord):
        results = []
        x = c.x
        y = c.y
        points = [Coord(x=x, y=y-1), Coord(x=x, y=y+1), Coord(x=x-1, y=y), Coord(x=x+1, y=y)]
        for p in points:
            if self.inBounds(p):
                results.append(p)
        return results

    def inBounds(self, c: Coord):
        x = c.x
        y = c.y
        return True if x >= 0 and x <= self.w and y >= 0 and y <= self.h else False

class Tile:
    @classmethod
    def map(cls, c:Coord, matrix, val):
        matrix[c.y, c.x] = val

    @classmethod
    def get(cls, c:Coord, matrix):
        return matrix[c.y, c.x]


class SnakeBody:
    def __init__(self, step, parent, body, food, direction):
        self.body = body
        self.direction = direction
        self.index = parent.index
        self.headValue = 0
        self.length = len(body)
        self.justAte = food
        self.parent = parent
        self.step = step

    def getHead(self):
        return self.body[0]

    def addSnakeToMatrix(self, bodyMatrix, removeTail):
        cnt = 0
        body = self.body.copy()
        if removeTail and len(body) >= 3:
            body.pop()
        for c in body:
            v = self.index
            if cnt == 0:
                v = -1
                if self.step > 0:
                    if self.parent.isDangerous:
                        v = -10
                    else:
                        v = 1
            prev = Tile.get(c, bodyMatrix)
            if prev != 0:
                # print('c has previous', c, prev)
                v = v + prev
            Tile.map(c, bodyMatrix, v)
            cnt = cnt + 1
        return bodyMatrix

    def __str__(self):
        ate = 'food' if self.justAte else ''
        return str('sb: {} {:<6} {:<6} body{}'.format(str(self.index), self.direction, ate, str(self.body)))

MY_SNAKE_INDEX = 1

class GameSnake:
    def __init__(self, index, data, bounds, refLen):
        self.index = index
        self.bounds = bounds
        self.data = data
        self.id = data.id
        self.step0 = SnakeBody(0, self, data.body, False, '')
        self.length = self.step0.length
        self.move = '' # TBD for mysnake.
        self.isMySnake = True if index == MY_SNAKE_INDEX else False
        self.isDangerous = True if not self.isMySnake and self.length >= refLen else False
        self.isPrey = True if not self.isMySnake and self.length < refLen else False

    def setupPossibleMoves(self, stepNumber, foodBoard, initialBoard):
        nextSnakes = []
        currentBody = self.step0
        head = currentBody.getHead()
        body = currentBody.body
        newHeads = []  # collect places to go that are legal and not occupied by any snake body part
        for newHead in self.bounds.getFourLegalPoints(head):
            if Tile.get(newHead, initialBoard) == 0: # space is not occupied by a body part
                newHeads.append(newHead)
        if len(newHeads) < 1:
            print("No where to go for this snake", self)
            self.move = 'up'

        for newHead in newHeads:
            dir = directionFromTo(head, newHead)
            food = Tile.get(newHead, foodBoard) != 0
            t1Body = [newHead] + body
            if len(t1Body) > 3:
                t1Body.pop()
            t1 = SnakeBody(stepNumber, self, t1Body, food, dir)
            nextSnakes.append(t1)
            print('add t1 snake:', t1)
        self.timeOneSnakes = nextSnakes

    def addTimeOneSnakesToBoard(self, board):
        for s in self.timeOneSnakes:
            s.addSnakeToMatrix(board, False)

    def chooseMove(self, board):
        if len(self.timeOneSnakes) == 0:
            return 'up'
        mv = -99
        for s in self.timeOneSnakes:
            h = s.getHead()
            v = Tile.get(h, board)
            s.headValue = v
            mv = max(v, mv)
            print('index, head, value: ', self.index, h, v)
        print('best value is ', mv)
        okMoves = []
        for s in self.timeOneSnakes:
            if s.headValue == mv:
                okMoves.append(s.direction)
        print('this way is ok', okMoves)
        self.move = random.choice(okMoves)
        return self.move

class GameBoard:
    def __init__(self, data: Game):
        self.data = data
        self.w = data.board.width
        self.h = data.board.height
        self.bounds = Bounds(self.w, self.h)

        # Create a empty board
        col = [0] * self.h
        self.board = np.array( [col] * self.w )

        foodBoard = self.board.copy()
        for c in data.board.food:
            Tile.map(c, foodBoard, 11)

        print('Food board:')
        print(foodBoard)

        # Set up the snakes
        # Index is just for dev and has no meaning. 1 is my snake. The rest start at 2
        index = MY_SNAKE_INDEX

        self.mySnake = GameSnake(index, self.data.you, self.bounds, 0)
        index = index + 1

        self.others = []
        for snake in self.data.board.snakes:
            if snake.id != self.mySnake.id:
                self.others.append(GameSnake(index, snake, self.bounds, self.mySnake.length))
                index = index + 1

        # Now combine all the snakes onto a board
        bodyParts = self.emptyBoard()
        self.mySnake.step0.addSnakeToMatrix(bodyParts, False)
        for snake in self.others:
            snake.step0.addSnakeToMatrix(bodyParts, False)
        print('Initial board:')
        print(bodyParts)

        # Now combine all the snakes onto a board
        step1BodyParts = self.emptyBoard()
        self.mySnake.step0.addSnakeToMatrix(step1BodyParts, True)
        for snake in self.others:
            snake.step0.addSnakeToMatrix(step1BodyParts, True)
        print('Step 1 body parts (no tails no new heads yet) board:')
        print(step1BodyParts)

        # next move
        step = 1
        self.mySnake.setupPossibleMoves(step, foodBoard, step1BodyParts)
        for snake in self.others:
            snake.setupPossibleMoves(step, foodBoard, step1BodyParts)

        # Now combine all the possible next move snakes onto a board
        moveOneBoard = self.emptyBoard()
        self.mySnake.addTimeOneSnakesToBoard(moveOneBoard)
        for snake in self.others:
            snake.addTimeOneSnakesToBoard(moveOneBoard)
        print('Move one board:')
        print(moveOneBoard)

        self.theMove = self.mySnake.chooseMove(moveOneBoard)

    def getReport(self):
        

    def dosome():
        # Next determine how my snake should move. Look for adjacent free space
        for step1Snake in self.mySnake.timeOneSnakes:
            h = step1Snake.getHead()
            hcnt = 0
            fourPoints = self.bounds.getFourLegalPoints(h)
            for p in fourPoints:
                if Tile.get(p, step1Parts) == 0:
                    hcnt += 1
                    print(step1Snake.index, 'head:', h, 'adj:', p, 'free', step1Snake.body)
            print(step1Snake.index, 'head:', h, hcnt, 'free', step1Snake.body)


        # Next determine how the snakes should move. Look for adjacent free space
        for snake in self.others:
            for step1Snake in snake.timeOneSnakes:
                h = step1Snake.getHead()
                hcnt = 0
                fourPoints = self.bounds.getFourLegalPoints(h)
                for p in fourPoints:
                    if Tile.get(p, step1Parts) == 0:
                        hcnt += 1
                        #print(step1Snake.index, 'head:', h, 'adj:', p, 'free')
                #print(step1Snake.index, 'head:', h, hcnt, 'free')

        # draft wip
        for y, col in enumerate(step1Parts):
            for x, v in enumerate(col):
                if v < 0:
                    fourPoints = self.bounds.getFourLegalPoints(Coord(x=x,y=y))
                    for p in fourPoints:
                        if Tile.get(p, step1Parts) == 0:
                            #print(x, y, 'free')
                            pass
    def emptyBoard(self):
        return self.board.copy()

