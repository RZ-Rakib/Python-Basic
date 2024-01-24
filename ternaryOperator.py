x = int(input("What is x? "))
y = int(input("What is y? "))
z = int(input("What is z? "))

max = (x if x > y and x > y else(y if y > z else z))
print(max)