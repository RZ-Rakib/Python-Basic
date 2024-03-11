# Basic example of zip

# two iterables or lists
name = ['Rakib', 'Niloy', 'Riyad', 'Sayeed']
age = [22, 23, 18, 25]

# combining elements from two lists into touples by using zip function
# zip function is a iteable object irtself, use list ....... to restore the new elemets
newTouplesList = list(zip(name, age))

print(f'New list with touples: {newTouplesList}')




# professional example of zip

# a matrix 
matrix=[
    ['Rakib', 'Niloy', 'Riyad', 'Sayeed'],
    [22, 23, 18, 25],
    ['B+', 'O-', 'B-', 'AB+']
]
# combining elements from two lists into touples by using zip function
# zip function is a iteable object irtself, use list ....... to restore the new elemets
newList = list(zip(*matrix))  # using Arbitrary positional argument '*' to unpack rows

print(f'New created list from matrix is : {newList}')