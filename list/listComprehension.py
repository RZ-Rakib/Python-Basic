# a list
numbers = [1, 2, 3, 4, 5, 6]

# comprehension map and filter 
# ['expression' 'map' 'filter']
newCompre = [x**2 for x in numbers if x % 2 == 0]
print(f'Here is the new list: {newCompre}')