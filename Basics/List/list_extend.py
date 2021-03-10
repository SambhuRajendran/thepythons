#This program shows how to append values of list from one to another
mufc = ["De Gea", "Rashford", "Cavani", "Bruno"]
madrid = ["Casmeiro", "Kroos", "Hazard"]
mufc.extend(madrid)
#here the values from madrid list will be added to mufc
print(mufc)
#extend can also add elements from Sets, dictionary, tuple etc
#Let's create a new tuple
barca = ('Messi', 'Busquets', 'Dembele')
#This will add tuple barca to previously extended list
mufc.extend(barca)
print(mufc)
