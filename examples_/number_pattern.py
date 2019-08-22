def pattern(numbers):
    for index in numbers:
        print("| ", end="")
        print('*' * int(index))


in_num = str(input("Enter the number to print pattern: "))
pattern(in_num)

