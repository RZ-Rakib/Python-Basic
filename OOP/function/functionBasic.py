def add(x, y):
    sum = x + y
    print(f'Addition is: {sum}')

def sub(x, y):
    sum = x - y
    print(f'Subtraction is: {sum}')
    
def mul(x, y):
    sum = x * y
    print(f'Multiplication is: {sum}')
    
def div(x, y):
    sum = x / y
    print(f'Divition is: {sum}')


userInput = ""
while userInput.lower() != "exit":
    userInput = input("Enter two diffrent numbers(press 'exit' to end): ")
    if userInput.lower().strip() == 'exit':
        break

    inputValue = userInput.split()

    num1 = int(inputValue[0])
    num2 = int(inputValue[1])

    add(num1, num2)
    sub(num1, num2)
    mul(num1, num2)
    div(num1, num2)
    
print(f'Program ended.')
