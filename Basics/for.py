#Players is a list () of dictionaries with key: name and value: pace
players = [
    {"name": "Rooney", "pace": 90},
    {"name": "Bruno", "pace": 77},
    {"name": "Rashford", "pace": 93},
    {"name": "Shaw", "pace": 80},
    
]

for player in players:
    #name variable will store the value for name attribute from player
    name = player["name"]
    #pace variable will store the value for the attrubute from player 
    pace = player["pace"]
    print(f'{name} has got {pace} sprint speed.')