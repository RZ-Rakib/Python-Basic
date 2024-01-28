'''
1. 1 + 2 + 3 + 4 + 5 + 6 + 7 + n
2. 2 + 4 + 6 + 8 + 10 + n
3. 1 + 3 + 5 + 7 + 9 + 10 + n
4. 1^2 + 2^2 + 4^2 + 5^2 + 6^2 + n^2
5. 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/n
6. prime number
'''

userInput = int(input("Enter the number: "))

text = ''
sum1 = 0

#1
for number1 in range(1, userInput + 1, 1):
    print(f"{text}{number1}")
    sum1 += number1 

print(f"Total sum of question no 1 is: {sum1}")

#2
sum2 = 0
for number2 in range(2, userInput + 1, 2):
    print(f"{text}{number2}")
    sum2 += number2
    
print(f"Total sum of question no 2 is: {sum2}")

#3
sum3 = 0
for number3 in range(1, userInput + 1, 2):
    print(f"{text}{number3}")
    sum3 += number3

print(f"Total sum of question no 3 is: {sum3}")

#4
sum4 = 0
for number4 in range(1, userInput + 1):
    square = number4 ** 2
    sum4 += square
    print(f"{text}{square}")

print(f"Total sum of question no 4 is: {sum4}")

#5 
sum5 = 0
for number5 in range(1, userInput + 1 ):
    newNum = 1 / number5
    print(f"{text}{newNum}")

print(f"Total sum of qustion no 5 is: {sum5}")

#prime number

endNumber = int(input("What is the end number: "))

for number in range(1 , endNumber + 1):
    if number > 1:
        for prime in range(2, int(number**0.5) + 1):
            if (number % prime) == 0:
                break 
        else:
            print(number)
        
    

            