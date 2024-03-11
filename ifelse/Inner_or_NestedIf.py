x = int(input("What is x? "))
y = int(input("What is Y? "))
z = int(input("What is z? "))

if x > y:

    if x > z:
        print(f"x is the largest number.")
    else:
        print(f"z is the largest number.")

else: # if y > x
    
    if y > z:
        print(f"y is the largest number.")
    else:
        print(f"z is the largest number.")