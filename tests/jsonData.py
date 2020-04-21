from pathlib import Path

filename = Path("tests/sample/board.json")
file = open(filename, "r")
json = file.read()
print(json)

def getBoardJson():
    return json

def obgetBoardJson():
    return '{\
        "height":11,"width":11,\
        "food":[{ "x":5, "y":1 },{ "x":1, "y":4 },{ "x":0, "y":8 }],\
        "snakes":[\
         {\
            "id":"s1", "name":"snake1", "health":100,\
            "body":[{"x":4,"y":1}, {"x":3,"y":1}, {"x":2,"y":1}],\
            "shout":"go for food at 5,1 or not? Change my health to see. See if s2 chooses a safer path?"\
         },\
         {\
            "id":"s2", "name":"snake2", "health":100,\
            "body":[{"x":2,"y":2}, {"x":1,"y":2}, {"x":0,"y":2}],\
            "shout":"In danger which way?"\
         },\
         {\
            "id":"s3", "name":"snake3", "health":45,\
            "body":[{"x":1,"y":3}, {"x":0,"y":3}],\
            "shout":"hungry go for food 1,4"\
         },\
         {\
            "id":"s4", "name":"snake4", "health":100,\
            "body":[{"x":3,"y":3}, {"x":3,"y":4}, {"x":3,"y":5}, {"x":3,"y":6}, {"x":3,"y":7}],\
            "shout":"big snake"\
         },\
         {\
            "id":"s5", "name":"snake5", "health":100,\
            "body":[{"x":6,"y":5}, {"x":5,"y":5},{"x":4,"y":5}],\
            "shout":"6,4 or 7,5 6,6"\
         }\
         {\
            "id":"s6", "name":"snake6", "health":100,\
            "body":[{"x":4,"y":6}, {"x":4,"y":4},{"x":4,"y":8}],\
            "shout":"4,5 or 3,6 5,6"\
         }\
         {\
            "id":"s7", "name":"snake7", "health":100,\
            "body":[{"x":1,"y":8}, {"x":1,"y":9}],\
            "shout":"not hungry avoid food at 0,8"\
         },\
        ]\
        }'



