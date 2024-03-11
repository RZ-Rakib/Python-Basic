'''
initialization
while condition:
    statements
    updates
'''

i = 1
while i <= 5:
    print('Rakib')
    i = i + 1


# this program will prompt user to press exit to end the program

userInput = ""

while userInput.lower() != 'exit':
    userInput = input("Enter a word (type 'exit' to end): ")
    print(f'You entered: {userInput}')

print(f'loop ended.')