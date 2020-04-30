#!/usr/bin/env bash


echo -n "Pick game 1, 2, 3, 4, 5, 6: "
read gm
case $gm in

    # best move is up into the space the tail is because right or down leads to danger
    # second option is to revisit the danger options previously discarded and pick the lesser of these options.
    [1] )
        curl -XPOST -H 'Content-Type: application/json' -d @tests/sample/game1.json http://localhost:8000/move
        ;;

    # test the flood algorithm with a bigger snake nearby that makes a wall
    [2] )
        curl -XPOST -H 'Content-Type: application/json' -d @tests/sample/game2.json http://localhost:8000/move
        ;;

    [3] )
        curl -XPOST -H 'Content-Type: application/json' -d @tests/sample/game3.json http://localhost:8000/move
        ;;

    # you're in the top most left corner. stay on the board!
    [4] )
        curl -XPOST -H 'Content-Type: application/json' -d @tests/sample/game4.json http://localhost:8000/move
        ;;

    # big snake caused out of bounds error
    [5] )
        curl -XPOST -H 'Content-Type: application/json' -d @tests/sample/game5.json http://localhost:8000/move
        ;;

    # go for food cause you'll starve otherwise!
    [6] )
        curl -XPOST -H 'Content-Type: application/json' -d @tests/sample/game6.json http://localhost:8000/move
        ;;


    *) echo "Invalid input"
        ;;
esac