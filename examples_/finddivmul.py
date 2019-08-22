# To find numbers divisible by 7 and multiples of 5
for number in range(1500, 2700):
    if number % 7 == 0 and number % 5 == 0:
        print(f'{number} is divisible  by 7 and 5')
    elif number % 5 == 0:
        print(f'{number} is a multiple of 5')
    elif number % 7 == 0:
        print(f'{number} is  divisible by 5')
    else:
        print('Number is not divisible')
