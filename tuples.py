# Baic example of tuples
fruits = ('Banana', 'Mango', 'Apple', 'Orange')

# Accessing elements
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# slice the tuples elements
print(fruits[1:3])

# we cannot update the tupel because it is mutable 
# Attempting to modify a tuple will result in an error
# fruits[0] = 'pear'  # This line will raise a TypeError

# concatenating tuples
new_fruits = ('Watermelon', 'Grape')
update_fruits = fruits + new_fruits
print(update_fruits)