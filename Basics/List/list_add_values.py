#here we are going to replace and  add values to a list

fifa = ["Ronaldo", "Messi", "Rooney", "Mane", "De Gea"]
#in the below line the value Rashford will replace at postion 1
# the postion [2] actually means [1] so player Pogba will be added
fifa[1:2] = ["Rashford", "Pogba"]
print(fifa)

#Here you can insert a value without replacing the current ones
fifa.insert(3, "Tevez")
#Value Tevez will be inserted after Rooney
print(fifa)
#