#!/usr/bin/env bash


echo -n "Pick game 1 or 2 or 3: "
read gm
case $gm in

    [1] )
        curl -XPOST -H 'Content-Type: application/json' -d @tests/sample/game1.json http://localhost:8000/move
        ;;

    [2] )
        curl -XPOST -H 'Content-Type: application/json' -d @tests/sample/game2.json http://localhost:8000/move
        ;;

    [3] )
        curl -XPOST -H 'Content-Type: application/json' -d @tests/sample/game3.json http://localhost:8000/move
        ;;

    *) echo "Invalid input"
        ;;
esac