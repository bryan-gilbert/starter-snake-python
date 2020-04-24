from pydantic import BaseModel
from app.models.snake import Snake
from app.models.board import Board

class GameId(BaseModel):
    id: str

class Game(BaseModel):
    game: GameId
    turn: int
    board: Board
    you: Snake

    def getId(self):
        return self.game.id

    def setup(self):
        self.board.setup()