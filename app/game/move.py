import json
import random

from typing import List
from app.models.models import Game, Coord

def moveSimple(data):
    print("move data: " + json.dumps(data))
    return {"move": 'up' }


def moveGame(game: Game):
    print("move game: " + game.game.id)
    print("move turn: " + str(game.turn))
    directions = ['up', 'down', 'left', 'right']
    value = game.turn % 12
    health = game.you.health
    print("value {:n} health {:n}".format(value, health))
    food = game.board.food[0]
    height = game.board.height
    width = game.board.width
    head = game.you.body[0]
    num_snakes = len(game.board.snakes)
    print("there are {} snakes on the board including you".format(num_snakes))
    avoid = buildAvoid(game)
    print(avoid)
    return {"move": 'up' }


def moveBest(data):
    print("move data: " + json.dumps(data))

    directions = ['up', 'down', 'left', 'right']
    value = data['turn'] % 12
    health = data['you']['health']
    food = data['board']['food'][0]
    height = data['board']['height']
    width = data['board']['width']
    head = data['you']['body'][0]
    avoid = []
    num_snakes = len(data['board']['snakes'])

    # appends the coordinates of the snakes to an array of coordinates to avoid
    for i in range(num_snakes):
        for j in range(len(data['board']['snakes'][i]['body'])):
            string = '(' + str(data['board']['snakes'][i]['body'][j]['x']) + "," + str(data['board']['snakes'][i]['body'][j]['y']) + ")"
            avoid.append(string)


    # appends the coordinates of the borders to the array of coordinates to avoid
    for i in range(height):
        string = "(" + '-1' + ',' + str(i) + ")"
        avoid.append(string)
        string = "(" + str(width) + ',' + str(i) + ")"
        avoid.append(string)
    for i in range(width):
        string = "(" + str(i) + ',' + '-1' + ")"
        avoid.append(string)
        string = "(" + str(i) + ',' + str(height) + ")"
        avoid.append(string)

    direction = random.choice(directions)
    # Finds food based on the first element in "food"
    # Goes left/right until the x matches, then goes up/down
    if health < 50:
        if food['x'] < head['x']:
            direction = 'left'
            print("err: 1")
        elif food['x'] > head['x']:
            direction = 'right'
            print("err: 2")
        elif food['x'] == head['x']:
            if food['y'] < head['y']:
                direction = "up"
                print("err: 3")
            elif food['y'] > head['y']:
                direction = 'down'
                print("err: 4")
    elif value == 0 or value == 1 or value == 2:
        direction = 'up'
        print("err: 6")
    elif value == 4 or value == 5 or value == 3:
        direction = 'right'
        print("err: 7")
    elif value == 7 or value == 8 or value == 6:
        direction = 'down'
        print("err: 8")
    elif value == 10 or value == 11 or value == 9:
        direction = 'left'
        print("err: 9")


    if direction == 'left':
        coord = "(" + str(head['x']-1) + ',' + str(head['y']) + ")"
    elif direction == 'right':
        coord = "(" + str(head['x']+1) + ',' + str(head['y']) + ")"
    elif direction == 'up':
        coord = "(" + str(head['x']) + ',' + str(head['y']-1) + ")"
    else:
        coord = "(" + str(head['x']) + ',' + str(head['y']+1) + ")"

    if coord in avoid:
        print("err: 10")
        direction = 'up'
        coord = "(" + str(head['x']) + ',' + str(head['y']-1) + ")"
        if coord in avoid:
            print("err: 11")
            direction = 'down'
            coord = "(" + str(head['x']) + ',' + str(head['y']+1) + ")"
            if coord in avoid:
                print("err: 12")
                direction = 'right'
                coord = "(" + str(head['x']+1) + ',' + str(head['y']) + ")"
                if coord in avoid:
                    print("err: 13")
                    direction = 'left'


    print("avoid: " + str(avoid))
    print("coord: " + coord)
    print("direc: " + direction)

    return {"move": direction }
