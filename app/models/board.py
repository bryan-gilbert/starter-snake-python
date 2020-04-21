from pydantic import BaseModel
from typing import List

from app.models.coord import Coord
from app.models.snake import Snake


class Board(BaseModel):
    height: int
    width: int
    food: List[Coord]
    snakes: List[Snake]

    def inBounds(self, coord:Coord):
        if coord.x < 0 : return False
        if coord.x > self.width-1 : return False
        if coord.y < 0 : return False
        if coord.y > self.height-1 : return False
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

    def selectTile(self, possibleTiles: List[Coord]):
        assert len(possibleTiles) > 0
        # TODO  improve this algorithm
        return possibleTiles[0]
