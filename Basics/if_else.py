#if-else
friends  = ['Jibu', 'Rekhin']
friends2 = ['KP', 'Jephin']

user_input = input('Enter a username: ')

if user_input in friends:
    print(f'Hello {user_input}!')
elif user_input in friends2:
    print(f'Hello {user_input}!')
else:
    print('Hello Stranger!')