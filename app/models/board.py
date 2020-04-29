from pydantic import BaseModel
from typing import List

from app.models.coord import Coord
from app.models.snake import Snake


class Board(BaseModel):
    height: int
    width: int
    food: List[Coord]
    snakes: List[Snake]
