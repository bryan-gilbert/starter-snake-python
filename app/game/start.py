
from app.models.game import Game

def startGame(game: Game):
    print('start with game', game)
    headType = 'bwc-earmuffs'
    tailType = 'bwc-ice-skate'
    color = "#add8e6"
    response = {"color": color, "headType": headType, "tailType": tailType}
    return response
