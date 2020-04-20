#!/usr/bin/env bash

curl -XPOST -H 'Content-Type: application/json' -d '
{
    "game": {"id": "game-id-string"},
    "turn": 4,
    "board": {"height": 15, "width": 15,
        "food": [{"x": 1,"y": 3}],
        "snakes": [
            {
            "id": "snake-id-string",
            "name": "BSnake",
            "health": 90,
            "body": [{"x": 1,"y": 3}],
            "shout": "Hello my name is BSnake"
            }
        ]
    },
    "you": {
        "id": "snake-id-string",
        "name": "BSnake",
        "health": 90,
        "body": [{"x": 1,"y": 3}],
        "shout": "Hello my name is BSnake"
    }
}' http://localhost:8000/move