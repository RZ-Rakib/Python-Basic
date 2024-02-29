def is_even(x):
    return x % 2 == 0

num = [1, 2, 3, 4, 5, 6]

# Using filter to keep only the even numbers in the list
# and converting the result to a list for immediate use or further manipulation.
result_list = list(filter(is_even, num))
print(f'The filtered list is: {result_list}')

# The filter function returns a filter object, which is an iterable.
# To obtain the results immediately or store them in a different container,
# you can use list(), tuple(), set(), or another iterable context.

# Example conversions:
result_list = list(filter(is_even, num))     # Convert to a list
result_tuple = tuple(filter(is_even, num))    # Convert to a tuple
result_set = set(filter(is_even, num))        # Convert to a set

# Alternatively, you can directly iterate over the filter object in a loop or another iterable context.

# Example iteration:
for value in filter(is_even, num):
    # Do something with each even value
    print(value)
