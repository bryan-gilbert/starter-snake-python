#!/usr/bin/env bash

curl -XPOST -H 'Content-Type: application/json' -d @tests/sample/game.json http://localhost:8000/move