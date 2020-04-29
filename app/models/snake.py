from pydantic import BaseModel
from typing import List
from app.models.coord import Coord

class Snake(BaseModel):
    id: str
    name: str
    health: int
    body: List[Coord]
    shout: str
