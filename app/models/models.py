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

class Board(BaseModel):
    height: int
    width: int
    food: List[Coord]
    snakes: List[Snake]

class Game(BaseModel):
    game: GameId
    turn: int
    board: Board
    you: Snake

    def myLength(self):
        return self.you.length()