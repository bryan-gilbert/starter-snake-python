import numpy as np
import random

from app.models.coord import Coord
from app.models.snake import Snake
from app.models.board import Board
from app.models.game import Game

TILE_SIZE = 10
EMPTY = '.' * TILE_SIZE
np.set_printoptions(linewidth=400)

HEAD = 'h'
TAIL = '-'
BODY = 'B'
FOOD = 'F'
BIG = 'd'
SMALL = 'p'
ME = '*'

UP = '^'
DWN = 'v'
LF = '>'
RH = '<'


MY_SNAKE_INDEX = ME

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

def headSymbol(body):
    # body is a list of coordinates with
    if len(body) < 2:
        return 'H'
    c2 = body[0]
    c1 = body[1]
    direction = ''
    assert c1 != c2
    if c2.x > c1.x:
        direction = '>'
    elif c2.x < c1.x:
        direction = '<'
    elif c2.y > c1.y:
        direction = 'v'
    else:
        direction = '^'
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
        matrix[c.y, c.x] = '{:^{TILE_SIZE}}'.format(val, TILE_SIZE=TILE_SIZE)

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

    def addSnakeToMatrix(self, bodyMatrix):
        body = self.body.copy()
        tailCnt = len(body) - 1
        for cnt, c in enumerate(body):
            index = self.index
            v = index + BODY
            if cnt == tailCnt:
                v = index + TAIL
            elif cnt == 0:
                v = index + HEAD + headSymbol(body)
                if self.step > 0:
                    if self.parent.isDangerous:
                        v = index + BIG + headSymbol(body)
                    elif self.parent.isPrey:
                        v = index + SMALL + headSymbol(body)
            prev = Tile.get(c, bodyMatrix)
            if prev != EMPTY and index not in prev:
                #print('c has previous', c, prev)
                v = v + prev.strip()
            Tile.map(c, bodyMatrix, v)
        return bodyMatrix

    def __str__(self):
        ate = 'food' if self.justAte else ''
        return str('sb: {} {:<6} {:<6} body{}'.format(str(self.index), self.direction, ate, str(self.body)))


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

    def setupPossibleMoves(self, stepNumber, initialBoard):
        nextSnakes = []
        currentBody = self.step0
        head = currentBody.getHead()
        body = currentBody.body
        newHeads = []  # collect places to go that are legal and not occupied by any snake body part
        for newHead in self.bounds.getFourLegalPoints(head):
            ct = Tile.get(newHead, initialBoard)
            if TAIL in ct or FOOD in ct or EMPTY in ct: # space is not occupied by a body part
                newHeads.append(newHead)
        if len(newHeads) < 1:
            print("No where to go for this snake", self)
            self.move = 'up'

        for newHead in newHeads:
            dir = directionFromTo(head, newHead)
            food = FOOD in Tile.get(newHead, initialBoard)
            t1Body = [newHead] + body
            if len(t1Body) > 3:
                t1Body.pop()
            t1 = SnakeBody(stepNumber, self, t1Body, food, dir)
            nextSnakes.append(t1)
            #print('add t1 snake:', t1)
        self.timeOneSnakes = nextSnakes

    def addTimeOneSnakesToBoard(self, board):
        for s in self.timeOneSnakes:
            s.addSnakeToMatrix(board)

    def chooseMove(self, board):
        if len(self.timeOneSnakes) == 0:
            return 'up'
        mv = -99
        for s in self.timeOneSnakes:
            h = s.getHead()
            v = Tile.get(h, board)
            s.headValue = v
            #mv = max(v, mv)
            print('index, head, value: ', self.index, h, v)
        print('best value is ', mv)
        okMoves = []
        #for s in self.timeOneSnakes:
        #    if s.headValue == mv:
        #        okMoves.append(s.direction)
        #print('this way is ok', okMoves)
        #self.move = random.choice(okMoves)
        #return self.move
        return 'up'

class GameBoard:
    def __init__(self, data: Game):
        self.data = data
        self.w = data.board.width
        self.h = data.board.height
        self.bounds = Bounds(self.w, self.h)

        # Create a empty board
        col = [EMPTY] * self.h
        self.board = np.array( [col] * self.w )

        for c in data.board.food:
            Tile.map(c, self.board, 'F')

        # Set up the snakes
        # Index is just for dev and has no meaning. 1 is my snake. The rest start at 2

        self.mySnake = GameSnake(MY_SNAKE_INDEX, self.data.you, self.bounds, 0)
        index = 1

        self.others = []
        for snake in self.data.board.snakes:
            if snake.id != self.mySnake.id:
                self.others.append(GameSnake(str(index), snake, self.bounds, self.mySnake.length))
                index = index + 1

        # Now combine all the snakes onto a board
        bodyParts = self.emptyBoard()
        self.mySnake.step0.addSnakeToMatrix(bodyParts)
        for snake in self.others:
            snake.step0.addSnakeToMatrix(bodyParts)
        print('Initial board:')
        print(bodyParts)

        # next move
        step = 1
        step1BodyParts = bodyParts
        self.mySnake.setupPossibleMoves(step, step1BodyParts)
        for snake in self.others:
            snake.setupPossibleMoves(step, step1BodyParts)

        # Now combine all the possible next move snakes onto a board
        moveOneBoard = self.emptyBoard()
        self.mySnake.addTimeOneSnakesToBoard(moveOneBoard)
        for snake in self.others:
            snake.addTimeOneSnakesToBoard(moveOneBoard)
        print('Move one board:')
        print(moveOneBoard)

        self.theMove = self.mySnake.chooseMove(moveOneBoard)

    def emptyBoard(self):
        return self.board.copy()
