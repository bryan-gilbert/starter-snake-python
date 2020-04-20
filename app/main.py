import json
import os
import random
from fastapi import Body, FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return '''
This is Zombie Snake.
Battlesnake documentation can be found at
<a href="https://docs.battlesnake.com">https://docs.battlesnake.com</a>.
'''

@app.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return {"success":"true"}


@app.post('/start')
def start(data = Body(...)):
    print('start with data', data)
    print(json.dumps(data))
    headType = 'bwc-earmuffs'
    tailType = 'bwc-ice-skate'
    color = "#add8e6"
    response = {"color": color, "headType": headType, "tailType": tailType}
    return response


@app.post('/move')
def move(data = Body(...)):
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


@app.post('/end')
def end():
    return {}


# You should use uvicorn to run the app locally.  __main__ is provided to run it in a debugger. See
# https://fastapi.tiangolo.com/tutorial/debugging/
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)


# Expose WSGI app (so gunicorn can find it)
#application = app.default_app()

#if __name__ == '__main__':
#    app.run(
#        application,
#        host=os.getenv('IP', '0.0.0.0'),
#        port=os.getenv('PORT', '8080'),
#        debug=os.getenv('DEBUG', True)
#    )
