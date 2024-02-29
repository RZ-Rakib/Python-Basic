from random import randint # randint generate new int between the limit, 
                           # but ramdom() generate float betwwen 0-1

count = 0
won = 0
loss = 0
for counts in range(1, 6):
    userInput = int(input("Guess the number(between 1-5): "))
    randomNumber = randint(1, 5)
    count += 1
    print(f"Attempt left: {5 - count}")
    
    if userInput == randomNumber:
        won += 1
        print("you are won.")
        print(f"Total won: {won}")
        print(f"Total loss: {loss}")

    else:
        loss += 1
        print("You are loss.")
        print(f"Total won: {won}")
        print(f"Total loss: {loss}")

print(f"Your attempts are finished.\nBetter luck next time.")