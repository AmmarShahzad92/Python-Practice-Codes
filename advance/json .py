import json 

disc = { "name": "disc",
        "age": 46,
        "exp": "2013"
        }

y = json.dumps(disc)
print(y)