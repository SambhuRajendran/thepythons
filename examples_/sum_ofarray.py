# Python Program to find sum of array and the maximum value in it.
def sum_of(values):
    return sum(values)


def max_of(max_value, n):
    n = len(max_value)
    max = max_value[0]
    for number in range(1, n):
        if max_value[number] > max:
            max = max_value[number]
    return max


n = int(input('Enter  the number of integers you want to add: '))
to_add = []
for count in range(n):
   num = int(input('Enter the number: '))
   to_add.append(num)
print('Sum of array is:', sum_of(to_add))
print('Maximum value of array is: ', max_of(to_add, n))


