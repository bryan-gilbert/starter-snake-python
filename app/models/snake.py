from pydantic import BaseModel
from typing import List
from app.models.coord import Coord

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

    def possibleMoveTiles(self, board):
        possible = self.validNextTiles(board)
        bodyParts = board.getBodyParts()
        tentative = []
        for c in possible:
            if c not in bodyParts:
                tentative.append(c)
        safe = []
        if len(tentative) > 0:
            dangerous = board.getDangerZones(self)
            for c in tentative:
                if c not in dangerous:
                    safe.append(c)
            if len(safe) == 0:
                safe = tentative
                self.shout = "Danger is exciting!?"
        else:
            safe = possible
            self.shout = "Brace for impact"
        return safe
