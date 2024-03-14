import re

pattern = r'RZ' # Define a regular expression pattern to search for words
text= "My name is RZ Rakib, I am from Bangladesh. I got 50€ from RZ" # Define a simple text string

matches = re.findall(pattern, text) # searching for the pattern in text

print(f"Found:", matches) # in findall function you cannot use group() and ifelse