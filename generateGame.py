import json
from app.game.game import moveGame
from app.models.game import Game

""" throw away code to generate a game and produce a json file for testing """

def saveGame(fName, jsonContent):
    file = open(fName, "w")
    file.write(json.dumps(jsonContent))

def getBaseSnake(id):
    return {"id":id, "name":id, "health":100,"body":[],"shout":""}

def getBaseGame():
    return {
        "game":{
            "id":"gameX"
        },
        "turn":0,
        "board":{
            "height":11,"width":11,
            "food":[],
            "snakes":[ ]
        },
        "you": {}
    }

def generateBoxedIn(gameId):
    game = getBaseGame()
    game['game']['id'] = gameId
    game['turn'] = 123
    my = getBaseSnake('mysnake')
    my['shout'] = 'This snake is boxed in if it turns left and will die as the head gets to 10,10. It needs to turn right to survive and that means looking out a long way'
    game['you'] = my
    other = getBaseSnake('othersnake')
    body = []
    x = 1
    for y in range(0,10):
        body.append({ "x":x, "y":y })
    y = 9
    for x in range(1,11): # up to col 10
        body.append({ "x":x, "y":y })
    x = 10
    for y in range(0,10)[::-1]:
        body.append({ "x":x, "y":y })
    y = 0
    for x in range(3,11)[::-1]:
        body.append({ "x":x, "y":y })
    my['body'] = body

    body = []
    x = 8
    for y in range(1,8)[::-1]:
        body.append({ "x":x, "y":y })
        pass
    y = 1
    for x in range(3,9)[::-1]:
        body.append({ "x":x, "y":y })
        pass
    x = 3
    for y in range(1,8):
        body.append({ "x":x, "y":y })
        pass
    y = 7
    for x in range(3,8):
        body.append({ "x":x, "y":y })
        pass
    other['body'] = body
    game['board']['snakes'].append(my)
    game['board']['snakes'].append(other)
    return game

def boxedIn():
    gameJson = generateBoxedIn('boxedIn')
    gameStr = json.dumps(gameJson)
    game = Game(**json.loads(gameStr))
    moveGame(game, gameJson)
    saveGame('boxedIn.json', gameJson)


def main():
    boxedIn()

if __name__=="__main__":
    main()