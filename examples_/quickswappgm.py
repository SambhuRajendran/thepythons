def swaparray(list_val):
    size = len(list_val)
    list_val[0], list_val[size-1] = list_val[size-1], list_val[0]
    print('Swapped Values: ', list_val)

lists=[]
n = int(input("Enter how many numbers you want in the list? "))
lists = [int(input('Enter the numbers: ')) for _ in range(n)]

swaparray(lists)

