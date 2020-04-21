#!/usr/bin/env bash

curl -XPOST -H 'Content-Type: application/json' -d '
{
   "game":{
      "id":"e3a8d180-1cfd-43fb-bff4-6b5f65a7e1f7"
   },
   "turn":0,
   "board":{
      "height":11,
      "width":11,
      "food":[
         {
            "x":3,
            "y":3
         },
         {
            "x":0,
            "y":9
         }
      ],
    "snakes":[
    {
    "id":"s1", "name":"snake1", "health":100,
    "body":[{"x":4,"y":1}, {"x":3,"y":1}, {"x":2,"y":1}],
    "shout":""
    },
    {
    "id":"s2", "name":"snake2", "health":100,
    "body":[{"x":2,"y":2}, {"x":1,"y":2}, {"x":0,"y":2}],
    "shout":""
    },
    {
    "id":"s3", "name":"snake3", "health":100,
    "body":[{"x":1,"y":3}, {"x":0,"y":3}],
    "shout":""
    },
    {
    "id":"s4", "name":"snake4", "health":100,
    "body":[{"x":3,"y":3}, {"x":3,"y":4}, {"x":3,"y":5}, {"x":3,"y":6}],
    "shout":""
    },
    {
    "id":"s5", "name":"snake5", "health":100,
    "body":[{"x":6,"y":5}, {"x":5,"y":5},{"x":4,"y":5}],
    "shout":""
    }
    ]
   },
   "you":{
    "id":"s2", "name":"snake2", "health":100,
    "body":[{"x":2,"y":2}, {"x":1,"y":2}, {"x":0,"y":2}],
    "shout":""
    }
}' http://localhost:8000/move