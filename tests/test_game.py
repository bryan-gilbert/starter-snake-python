import json
from app.models.models import Game, Coord
from jsonData import getGameJson

class TestGame:

    def test_gameFromJson(self):
        gameJSON = getGameJson()
        game = Game(**json.loads(gameJSON))
        assert game.board.width == 11
        assert game.you.health == 100
        assert game.you.body[0] == Coord(x=9, y=1)
