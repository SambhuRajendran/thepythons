#iterating through the dictionary values

player_attributes = {"messi": 93, "Rooney": 90, "Ronaldo": 93}

for values in player_attributes.values():
    #player_attributes.values() will print the values
    print(values)
for playername, overall in player_attributes.items():
    #.items can print both key and value
    print(f'{playername} has got {overall} stats ')

   