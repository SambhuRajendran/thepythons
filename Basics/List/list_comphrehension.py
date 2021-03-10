userinput = input("name???")
our_list = ['krishna', 'rekhin', 'sambhu' ]

names_lower_list = [name.lower() for name in our_list]

print(names_lower_list)
if userinput.lower() in names_lower_list:
    print(f"{userinput.lower()} is ur friend")
