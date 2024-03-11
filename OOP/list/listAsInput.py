# Variable initialize
userInput  = ""
totalWords = 0
totalLetters = 0
totalNumbers = 0 

# User input loop
while userInput.lower() != 'exit':
    userInput = input("Write anything(type 'exit' to end program): ")
    print(f"You entered: {userInput}")

# Reset counts for each input
    totalWords = 0
    totalLetters = 0
    totalNumbers = 0 
# For loop to iterates each character
    for x in userInput:
        x.lower()

        if x >= 'a' and x <= 'z':
            totalLetters = totalLetters + 1
        elif x >= '0' and x <= '9':
            totalNumbers = totalNumbers + 1
            
# counting words by spilting on spaces
    totalWords = len(userInput.split())

    print(f'Number of words: {totalWords}')
    print(f'Number of letters: {totalLetters}')
    print(f'Number of words: {totalWords}')


print("Loop ended.")

