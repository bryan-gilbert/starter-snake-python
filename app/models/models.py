from pydantic import BaseModel
from typing import List

class GameId(BaseModel):
    id: str

class Coord(BaseModel):
    x: int
    y: int

class Snake(BaseModel):
    id: str
    name: str
    health: int
    body: List[Coord]
    shout: str

    def length(self):
        return len(self.body)

    def validNextTiles(self, board):
        """ Provides list of valid next move coordinates for this snake.
        Excludes coordinates that our out of bounds.
        Excludes coordinates that are in this snakes body.
        """
        height = board.height
        width = board.width
        body = self.body
        head = body[0]
        body = body[1] if len(body) > 1 else None
        isValid = lambda coord : body != coord and board.inBounds(coord)
        validCoords: List[Coord] = []
        # up
        coord = Coord(x = head.x, y = head.y -1)
        if isValid(coord) : validCoords.append(coord)
        # down
        coord = Coord(x = head.x, y = head.y + 1)
        if isValid(coord) : validCoords.append(coord)
        # left
        coord = Coord(x = head.x - 1, y = head.y)
        if isValid(coord) : validCoords.append(coord)
        # right
        coord = Coord(x = head.x + 1, y = head.y)
        if isValid(coord) : validCoords.append(coord)
        return validCoords

    def nextMove(self, board):
        possible = self.validNextTiles(board)
        return possible


class Board(BaseModel):
    height: int
    width: int
    food: List[Coord]
    snakes: List[Snake]

    def inBounds(self, coord:Coord):
        if coord.x < 0 : return False
        if coord.x > self.width : return False
        if coord.y < 0 : return False
        if coord.y > self.height : return False
        return True

    def getBodyParts(self):
        # appends the coordinates of the snakes to an array of coordinates to avoid
        avoid:List[Coord] = []
        snakes = self.snakes
        num_snakes = len(snakes)
        for i in range(num_snakes):
            aSnake = snakes[i]
            for j in range(len(aSnake.body)):
                pos = aSnake.body[j]
                avoid.append(pos)
        return avoid

    def getDangerZones(self,forSnake):
        # appends the coordinates of the tiles where dangerous snakes may place their head in the next move
        avoid:List[Coord] = []
        forSnakeSize = forSnake.length()
        forSnakeId = forSnake.id
        snakes = self.snakes
        num_snakes = len(snakes)
        for i in range(num_snakes):
            aSnake = snakes[i]
            if aSnake.id != forSnake.id and aSnake.length() >= forSnake.length() :
                nextTiles = aSnake.validNextTiles(self)
                avoid += nextTiles
        return avoid

class Game(BaseModel):
    game: GameId
    turn: int
    board: Board
    you: Snake

    def myLength(self):
        return self.you.length()
