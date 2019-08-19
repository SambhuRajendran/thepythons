def find(list_val, y):
    if y in list_val:
        index = list_val.index(y)
        print(f'The number is in position: {index}')
    else:
        print('Number not found!')


lists = []
n = int(input("Enter how many numbers you want in the list? "))
lists = [int(input('Enter the numbers: ')) for _ in range(n)]
x = int(input("Enter the number to find: "))

# Calling the function here
find(lists, x)
