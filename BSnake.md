# Extra notes

Cloned from [https://github.com/BattlesnakeOfficial/starter-snake-python](https://github.com/BattlesnakeOfficial/starter-snake-python)

Converted to use FastAPI

Converted to use Heroku

## Heroku setup

I assume you have heroku account and have installed the heroku CLI

1) Login once in your terminal
```
Heroku login
```

2) Create your app once
```
heroku create yourGreatSnake
```

```yourGreatSnake``` is your heroku app name

You will see this results in two urls

3) Tell heroku you wish to use git, once

```
heroku git:remote -a yourAppName
```

To delete your app


## Heroku update

After making any code adjustments you need to push your changes up to heroku. This will trigger a rebuild of your server.

1)  Add your changes to the git staging and then commit and then push to heroku

```bash
git add .
git commit -m"snake"
git push heroku master
```

Or in one line 
```
git add . && git commit -m"snake" && git push heroku master
```

## Optionals
Run local server:
```
python app/main.py
```

To test your server


```
curl -XPOST -H 'Content-Type: application/json' -d '{ "hello": "world"}' http://localhost:8000/start
```

```
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
```


