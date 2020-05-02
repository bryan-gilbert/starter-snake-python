# A [Battlesnake](http://play.battlesnake.com) written in Python.


Cloned from [https://github.com/BattlesnakeOfficial/starter-snake-python](https://github.com/BattlesnakeOfficial/starter-snake-python)

Converted to use FastAPI with Pydantic.

This is a reasonably sophisticated snake. It does not use ML or AI and instead works with some simple algorithms
(e.g flood) and heuristics.  


## Run
Run local server with nodemon (which watches for code changes and restarts your app automatically)
```
nodemon --exec python3 main.py 

```

## Test

```
./unitTest.sh
```
This shell runs pytest which runs all the tests in the tests folder. This includes several tests that current fail. 
These are just showing Test Driven Development. You build your tests. Your code fails your tests. You develop 
new code that handles the requirements set out by the tests.

```
./tests/scripts/moveGame.sh
```
This shell script lets you send a game via curl to your local server


### Technologies

This Battlesnake uses [Python 3.7](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com/), [Pydantic](https://pydantic-docs.helpmanual.io/) and [Heroku](https://heroku.com).


# Files

Procfile is for Heroku

main.py is the main server

generateGame.py can be used and modified to create more complex sample games for testing.

