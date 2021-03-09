cars = ["ok","ok","ok","faulty", "ok", "ok"]
for status in cars:
    if status == "faulty":
        print(f"Car is {status}, skipping ")
        continue
    else:
        print(f'This car is {status}')    
    #print(f"This car is {status}")
#else can be used for 'for' and 'while'
else:
    print("Checking completed............")
