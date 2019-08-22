# Program to find % of a number


def percentage():
    print("Program to find percentage of a number ")
    print("Format is P% of X")
    p = int(input("Enter the % value for (P Value): "))
    x = int(input('Enter the number to find the percentage of(X Value) :'))
    perc = p/100
    value = x * perc
    print('Percentage  of  the  value is: ', value)


percentage()