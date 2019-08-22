numbers = (2,3,5,6,7)
odd = 0
even = 0
for num in numbers:
    if num % 2 == 0:
        print(f'{num} is  even')
        even = even+1
    else:
        print(f'{num} is odd')
        odd = odd + 1

print(f'There are {odd} odd and {even} even numbers in the list')