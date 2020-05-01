from fastapi.testclient import TestClient
from pathlib import Path
import json
import os

from main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/")
    assert response.status_code == 200
    rjson = response.json()
    print('response.json()', rjson)
    assert rjson['name'] == 'zombie snake'


def util_move_file(fName, expected, reason):
    path = os.path.join('.', 'tests', 'sample', fName)
    with open(path, 'r') as gameFile:
        jsonData = gameFile.read()
    data = json.loads(jsonData)
    response = client.post("/move",json=data)
    rjson = response.json()
    print('response.json()', rjson)
    assert response.status_code == 200
    assert rjson['move'] == expected, "expected move {} because {}".format(expected, reason)

def test_move1():
    # best move is up into the space the tail is because right or down leads to danger
    # second option is to revisit the danger options previously discarded and pick the lesser of these options.
    fName = 'game1.json'
    expected = 'up'
    reason = 'Expect the tail to move and make room'
    util_move_file(fName, expected, reason)

""" This test fails """
def test_move1():
    # test the flood algorithm with a bigger snake nearby that makes a wall
    fName = 'game1.json'
    expected = 'up'
    reason = 'Expect the tail to move.'
    util_move_file(fName, expected, reason)

def test_move2():
    fName = 'game2.json'
    expected = 'down'
    reason = 'Most space is down.'
    util_move_file(fName, expected, reason)

def test_move3():
    fName = 'game3.json'
    expected = 'up'
    reason = 'Expect the tail to move.'
    util_move_file(fName, expected, reason)

def test_move4():
    fName = 'game4.json'
    expected = 'down'
    reason = 'you are in the top most left corner. stay on the board!'
    util_move_file(fName, expected, reason)

def test_move5():
    # big snake caused out of bounds error
    fName = 'game5.json'
    expected = 'up'
    reason = 'Expect the tail to move.'
    util_move_file(fName, expected, reason)

def test_move6():
    fName = 'game6.json'
    expected = 'up'
    reason = 'go for food cause you will starve otherwise!'
    util_move_file(fName, expected, reason)

""" This test fails """
def test_move7():
    # as this is added my snake doesn't know that the best move is to go for the smaller snake. Instead
    # it just doesn't have a clue and turns right into the bigger snake
    fName = 'game7.json'
    expected = 'up'
    reason = 'go for smaller snake and stay away from the bigger snake'
    util_move_file(fName, expected, reason)

""" This test fails """
def test_move8():
    # as this is added my snake makes a right turn into the head of a bigger snake. It should go down or left.
    fName = 'game8.json'
    expected = 'down'
    reason = 'stay away from bigger snake. go down or left'
    util_move_file(fName, expected, reason)


""" This test fails """
def test_move_boxedIn():
    # as this is added my snake makes a left and will eventually collide with itself.
    fName = 'boxedIn.json'
    expected = 'right'
    reason = 'This snake is boxed in if it turns left and will die as the head gets to 10,10. It needs to turn right to survive and that means looking out a long way'
    util_move_file(fName, expected, reason)
