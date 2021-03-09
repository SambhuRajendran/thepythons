user_input = input("Do you wish to continue?? (Yes/No)")
#.title is used to make the first letter upper-case
capitalizer = user_input.title()
while  capitalizer == "Yes":
    print("We are running!")
    user_input = input("Do you still wish to continue?")
    #This CAPITALIZER function is used to conver the input from previous line to title() format
    capitalizer = user_input.title()

print("we are done!")