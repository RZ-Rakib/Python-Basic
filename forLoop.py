numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

text = ""
index = 0
sum = 0
'''while index < len(numbers):
    print(f'{text} {numbers[index]}')
    index += 1'''

for number in numbers:
    print(f'{text}{index + 1} = {numbers[index]}')
    index += 1
    sum += number

print(f'total sum is {sum}')