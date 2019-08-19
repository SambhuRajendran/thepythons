<<<<<<< HEAD:examples_/oldswap_array.py
############old
=======
##############THIS IS AN OLD METHOD##################
>>>>>>> 8761a0fcd23a0e75499879e475b41f822d2362ed:examples_/array.py
#listof get input from the user
listof = []
#n is the number of values  that user wants to add to array
n= int(input("Enter the length of your list: "))

for i in range(0,n):
    x = int(input('Enter the numbers? '))
    #Appends the value entered by user to the 'listof' variable
    listof.append(x)
    print(x)

size = len(listof)
print('Original List: ', listof)
#storing the value of 0th position to a temp variable
temp = listof[0]
#Then replacing the first value with the (n-1)th value of the size
listof[0]=listof[size - 1]
#changing the (n-1)th value to the temp variable
listof[size - 1]= temp
#saving the value of temp to 0th value of the list
temp = listof[0]
print('New swapped  list: ', listof)

