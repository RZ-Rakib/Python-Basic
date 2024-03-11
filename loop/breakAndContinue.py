num = int(input("Enter the number: "))
sum = 0
i = 1

while i <= num :
  
    if i == 5:
        i = i + 1
        continue
    if i == 10:
        break
    sum = sum + i
    i = i + 1

print(f'The total sum is {sum}.')