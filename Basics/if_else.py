#if-else
friends  = ['Jibu', 'Rekhin']
friends2 = ['KP', 'Jephin']

user_input = input('Enter a username: ')

#The follwing condition checks in if and elif will look for the values in variables friends and friends2
if user_input in friends:
    print(f'Hello {user_input}!')
elif user_input in friends2:
    print(f'Hello {user_input}!')
else:
    print('Hello Stranger!')