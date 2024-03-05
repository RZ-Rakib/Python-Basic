# read a file "r" 0r "r+"  to both read and write
file = open("example.txt", "r") # call a file and restore in a new variable

print(file.readable()) # to check the file is readable or not

# readFile = file.read() # to print the exact text
# print(readFile)

# file.seek(0)  # Move the file cursor to the beginning

readFile_as_text = file.readlines()[1] # to convert txt file into a list, add an index number to print a specific line
print(readFile_as_text)


print(f'total character\'s length = {len(readFile_as_text)}')

file.close() # it is a good practice to close the file 


# write a file "w"
# file = open("example.txt", "w") # call a file and restore in a new variable

# print(file.writeable()) # to check the file is readable or not
# file.close() # it is a good practice to close the file 


''' 
Use "r+" instead of "r" or "w" to open the file for both reading and writing.
'''

# append new line in the existing .txt file
file2 = open("example2.txt", 'a') # if use "w" it will overwite the actual text
file2.write("\nI am using append function and my name is new line")

file2.close()


# create a new file txt, html or anything 
file3 = open("example3.txt", 'w') # write the file name and use "w"
file3.write("\nI am using append function and my name is new file example3.txt")

file3.close()
