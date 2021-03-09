for n in range(2,15):
    #print(f'n is {n}')
    for x in range (2,n):
       # print(f'x is {x}')
        if n % x == 0:
            print(f'number{n} is not prime')
    else:
        print(f'Number  {n} is prime')

