# Print star pattern
star = int(input("enter number of  star: "))
for fstar in range(1, star):
    print(fstar*'*')
    if fstar == star - 1:
        for rstar in range(star, 0, -1):
            print(rstar*'*')

