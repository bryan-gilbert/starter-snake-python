def getSnakeJson():
    return '{\
        "id":"gs_mc978CBx7tYKCd3B9cbXJgWB",\
        "name":"Zombie Snake",\
        "health":100,\
        "body":[\
         {\
            "x":9,\
            "y":1\
         },\
         {\
            "x":9,\
            "y":1\
         },\
         {\
            "x":9,\
            "y":1\
         }\
        ],\
        "shout":""\
        }'

def getBoardJson():
    return '{\
        "height":11,\
        "width":11,\
        "food":[\
           { "x":3, "y":3 },\
           { "x":0, "y":9 }\
        ],\
        "snakes":[]}'


def getGameJson() :
    return '{\
       "game":{\
          "id":"e3a8d180-1cfd-43fb-bff4-6b5f65a7e1f7"\
       },\
       "turn":0,\
       "board":{\
          "height":11,\
          "width":11,\
          "food":[\
             {\
                "x":3,\
                "y":3\
             },\
             {\
                "x":0,\
                "y":9\
             }\
          ],\
          "snakes":[\
             {\
                "id":"gs_vYMK3fVwDbM4JMJTqGQVwPwJ",\
                "name":"simple-sample-snake",\
                "health":100,\
                "body":[\
                   {\
                      "x":1,\
                      "y":5\
                   },\
                   {\
                      "x":1,\
                      "y":5\
                   },\
                   {\
                      "x":1,\
                      "y":5\
                   }\
                ],\
                "shout":""\
             },\
             {\
                "id":"gs_mc978CBx7tYKCd3B9cbXJgWB",\
                "name":"Zombie Snake",\
                "health":100,\
                "body":[\
                   {\
                      "x":9,\
                      "y":1\
                   },\
                   {\
                      "x":9,\
                      "y":1\
                   },\
                   {\
                      "x":9,\
                      "y":1\
                   }\
                ],\
                "shout":""\
             }\
          ]\
       },\
       "you":{\
          "id":"gs_mc978CBx7tYKCd3B9cbXJgWB",\
          "name":"Zombie Snake",\
          "health":100,\
          "body":[\
             {\
                "x":9,\
                "y":1\
             },\
             {\
                "x":9,\
                "y":1\
             },\
             {\
                "x":9,\
                "y":1\
             }\
          ],\
          "shout":""\
       }\
    }'
