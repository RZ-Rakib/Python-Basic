letter = input("What is the letter? ")
lowerLetter = letter.lower()

# len(lowerLetter) == 1 will check that user is entering one charecter
# .isalpha will check that user is entering the alphabet instead of numbers or special charecter
if len(lowerLetter) == 1 and lowerLetter.isalpha():

    if lowerLetter == 'a' or lowerLetter == 'e' or lowerLetter == 'i' or lowerLetter == 'o' or lowerLetter == 'u':
        print(f'{letter} is a vowel.') 
    else:
        print(f'{letter} is a consonant.')

else:
    print(f'Please enter a single alphabet charecter.')