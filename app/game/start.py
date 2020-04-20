import json
from app.models.models import Game


def startGame(game: Game):
    print('start with game', game)
    print('my length' + str(game.myLength()))
    #print('game', data['game']['id'])
    headType = 'bwc-earmuffs'
    tailType = 'bwc-ice-skate'
    color = "#add8e6"
    response = {"color": color, "headType": headType, "tailType": tailType}
    return response
