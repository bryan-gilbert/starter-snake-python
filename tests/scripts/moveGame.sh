#!/usr/bin/env bash


echo -n "Pick game 1, 2, 3, 4, 5: "
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

    [4] )
        curl -XPOST -H 'Content-Type: application/json' -d @tests/sample/game4.json http://localhost:8000/move
        ;;

    [5] )
        curl -XPOST -H 'Content-Type: application/json' -d @tests/sample/game5.json http://localhost:8000/move
        ;;


    *) echo "Invalid input"
        ;;
esac