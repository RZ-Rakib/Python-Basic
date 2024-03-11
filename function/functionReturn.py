def add(x, y):
    sum = x + y
    return sum

def sub(x, y):
    sum = x - y
    return sum
    
def mul(x, y):
    sum = x * y
    return sum
    
def div(x, y):
    sum = x / y
    return sum 

userInput = ""
while userInput.lower() != "exit":
    userInput = input("Enter two diffrent numbers(press 'exit' to end): ")
    if userInput.lower().strip() == 'exit':
        break

    inputValue = userInput.split()

    num1 = int(inputValue[0])
    num2 = int(inputValue[1])

    print(f'Addition is: {add(num1, num2)}')
    print(f'Addition is: {sub(num1, num2)}')
    print(f'Addition is: {mul(num1, num2)}')
    print(f'Addition is: {div(num1, num2)}')
    
print(f'Program ended!')
