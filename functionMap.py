def square(x):
    return x ** 2

num = [1, 2, 3, 4, 5, 6]

# Using map to apply the square function to each element in the list
# and converting the result to a list for immediate use or further manipulation.
result_list = list(map(square, num))
print(f'The new list is: {result_list}')

# The map function returns a map object, which is an iterable.
# To obtain the results immediately or store them in a different container,
# you can use list(), tuple(), set(), or another iterable context.

# Example conversions:
result_list = list(map(square, num))     # Convert to a list
result_tuple = tuple(map(square, num))    # Convert to a tuple
result_set = set(map(square, num))        # Convert to a set

# Alternatively, you can directly iterate over the map object in a loop or another iterable context.

# Example iteration:
for value in map(square, num):
    # Do something with each squared value
    print(value)
