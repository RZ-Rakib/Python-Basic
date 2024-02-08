# Basic example of set
mySet1 = {1, 2, 3, 'apple', 'banana', 'orange'}
print(mySet1)

# Iterating through the set
for element in mySet1:
    print(element)


# Procedures for creating set
mySet2 = {'Rakib', 'Niloy', 'Riyad'}  # Curly braces are required
mySet3 = set(['Rakib', 'Niloy', 'Riyad', 'Sayeed'])  # Use set constructor to convert a list to a set
mySet4 = set(('Rakib', 'Niloy', 'Riyad', 'Sayeed'))  # Use set constructor to convert tuples to a set

print(f"Procedures section codes: {mySet2}\n{mySet3}\n{mySet4}")


# Professional example of set
mySet5 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 14}
mySet6 = {1,2, 3, 5, 7, 9, 10, 20}
mySet7 = {2, 3, 4, 6, 8, 10, 25}

# Union operation
unionSet1 = mySet5.union(mySet6, mySet7)
unionSet2 = mySet5 | mySet6 | mySet7  # Alternative way
print(f'Union: {unionSet1}\n{unionSet2}')

# Intersection operation
intersectionSet1 = mySet5.intersection(mySet6, mySet7)
intersectionSet2 = mySet5 & mySet6 & mySet7  # Alternative way
print(f'Intersection: {intersectionSet1}\n{intersectionSet2}')

# Difference operation and it will only the difference present in the first set
differenceSet1 = mySet5.difference(mySet6, mySet7)
differenceSet2 = mySet5 - mySet6 - mySet7  # Alternative way
print(f'Difference: {differenceSet1}\n{differenceSet2}')

# Symmetric_difference operation to find unique differences among all three sets
symmetricDifferenceSet1 = mySet5.symmetric_difference(mySet6).symmetric_difference(mySet7)
# Symmetric_difference operation using the ^ operator, it is an alternative way
symmetricDifferenceSet2 = mySet5 ^ mySet6 ^ mySet7
print(f'Symmetric Difference: {symmetricDifferenceSet1}\n{symmetricDifferenceSet2}')


# Empty set vs empty dictionary
emptySet = set()  # Empty set requires set constructor
emptyDictionary = {}  # Only curly braces create an empty dictionary
