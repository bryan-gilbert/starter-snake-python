from pydantic import BaseModel

class Coord(BaseModel):
    x: int
    y: int

    @classmethod
    def directionFromTo(cls, c1:'Coord', c2:'Coord'):
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
